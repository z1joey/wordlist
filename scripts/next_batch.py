#!/usr/bin/env python3
"""Pick the next batch of words for the dictionary review plan.

Usage:
    python3 scripts/next_batch.py --size 500 --phase auto > batch-001.json

The output is JSON, ready to be consumed by the producer / verifier.
Schema (input = progress.json + the 26 dict files, output = batch spec):
{
  "batch_id": 1,
  "phase": "A",
  "size": 500,
  "picked_at": "2026-06-25T16:55:00",
  "items": [
    {"file": "a.json", "index": 123, "word": "example", "tags": ["cet4"], "score": 47}
  ]
}

Priority (§2 of PLAN.md):
  Phase A: tagged words, score = len(tags)*10 + empty_senses*2 + dupes
  Phase B: untagged words that have at least one duplicate sense translation
  Phase C: untagged words with empty translations
  "auto" walks A -> B -> C.

Excludes any (file, index) pair already listed in a committed batch in
progress.json, so re-running this script is safe.

Run from /Users/joey/wordlist/.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROGRESS = ROOT / "progress.json"


def load_progress() -> dict[str, Any]:
    if not PROGRESS.exists():
        return {"schema_version": 1, "next_batch_id": 1, "totals": {}, "batches": []}
    with PROGRESS.open() as f:
        return json.load(f)


def already_done_set(progress: dict[str, Any]) -> set[tuple[str, int]]:
    done: set[tuple[str, int]] = set()
    for batch in progress.get("batches", []):
        if batch.get("status") != "committed":
            continue
        for fname, indices in batch.get("word_indices", {}).items():
            for i in indices:
                done.add((fname, int(i)))
    return done


def score_word(rec: dict[str, Any]) -> tuple[int, int, int]:
    """Return (tag_score, empty_count, dup_count) for a single word record."""
    tags = rec.get("tags") or []
    empty = 0
    for entry in rec.get("entries", []):
        for s in entry.get("senses", []):
            if not (s.get("translation") or "").strip():
                empty += 1
    trs = [
        s.get("translation", "").strip()
        for entry in rec.get("entries", [])
        for s in entry.get("senses", [])
        if (s.get("translation") or "").strip()
    ]
    cnt = Counter(trs)
    dup = sum(v - 1 for v in cnt.values() if v > 1 and len(cnt) > 1)
    return (len(tags) * 10, empty, dup)


def has_duplicate(rec: dict[str, Any]) -> bool:
    trs = [
        s.get("translation", "").strip()
        for entry in rec.get("entries", [])
        for s in entry.get("senses", [])
        if (s.get("translation") or "").strip()
    ]
    cnt = Counter(trs)
    return any(v >= 2 for v in cnt.values()) and len(cnt) > 1


def has_empty(rec: dict[str, Any]) -> bool:
    for entry in rec.get("entries", []):
        for s in entry.get("senses", []):
            if not (s.get("translation") or "").strip():
                return True
    return False


def iter_words():
    for f in sorted(ROOT.glob("[a-z].json")):
        with f.open() as fp:
            data = json.load(fp)
        for idx, rec in enumerate(data):
            yield f.name, idx, rec


def pick_phase_a(done: set[tuple[str, int]], size: int) -> list[dict[str, Any]]:
    """Tagged words, priority by score."""
    candidates: list[tuple[tuple[int, int, int], str, int, dict]] = []
    for fname, idx, rec in iter_words():
        if (fname, idx) in done:
            continue
        if not rec.get("tags"):
            continue
        sc = score_word(rec)
        # Sort key: (tag_score, empty_count, dup_count) all descending
        candidates.append(((sc[0], sc[1], sc[2]), fname, idx, rec))
    candidates.sort(key=lambda t: (-t[0][0], -t[0][1], -t[0][2], t[1], t[2]))
    out = []
    for _sc, fname, idx, rec in candidates[:size]:
        out.append({
            "file": fname,
            "index": idx,
            "word": rec.get("word", f"#{idx}"),
            "tags": rec.get("tags", []),
            "score": {
                "tag": _sc[0] // 10,
                "empty_senses": _sc[1],
                "duplicates": _sc[2],
            },
        })
    return out


def pick_phase_b(done: set[tuple[str, int]], size: int) -> list[dict[str, Any]]:
    candidates = []
    for fname, idx, rec in iter_words():
        if (fname, idx) in done:
            continue
        if rec.get("tags"):
            continue  # Phase A territory
        if not has_duplicate(rec):
            continue
        candidates.append((fname, idx, rec))
    # Sort by dup severity, then word length (proxy for complexity)
    candidates.sort(key=lambda t: (-sum(1 for _ in (
        s for e in t[2].get("entries", [])
        for s in e.get("senses", [])
    )), t[0], t[1]))
    out = []
    for fname, idx, rec in candidates[:size]:
        out.append({
            "file": fname,
            "index": idx,
            "word": rec.get("word", f"#{idx}"),
            "tags": rec.get("tags", []),
            "score": {"phase": "B", "reason": "untagged_with_duplicates"},
        })
    return out


def pick_phase_c(done: set[tuple[str, int]], size: int) -> list[dict[str, Any]]:
    candidates = []
    for fname, idx, rec in iter_words():
        if (fname, idx) in done:
            continue
        if rec.get("tags"):
            continue
        if not has_empty(rec):
            continue
        candidates.append((fname, idx, rec))
    candidates.sort(key=lambda t: (t[0], t[1]))
    out = []
    for fname, idx, rec in candidates[:size]:
        out.append({
            "file": fname,
            "index": idx,
            "word": rec.get("word", f"#{idx}"),
            "tags": rec.get("tags", []),
            "score": {"phase": "C", "reason": "untagged_with_empty"},
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=500)
    ap.add_argument(
        "--phase",
        choices=["auto", "A", "B", "C"],
        default="auto",
        help="auto walks A->B->C based on progress.json",
    )
    ap.add_argument("--json", action="store_true", help="emit JSON (default)")
    args = ap.parse_args()

    progress = load_progress()
    done = already_done_set(progress)
    batch_id = int(progress.get("next_batch_id", 1))

    pickers = {"A": pick_phase_a, "B": pick_phase_b, "C": pick_phase_c}
    phase = args.phase
    if phase == "auto":
        for p in ("A", "B", "C"):
            items = pickers[p](done, args.size)
            if items:
                phase = p
                break
        else:
            print(json.dumps({"batch_id": batch_id, "phase": None, "items": []}, indent=2))
            return 0

    items = pickers[phase](done, args.size)
    out = {
        "batch_id": batch_id,
        "phase": phase,
        "size": args.size,
        "picked_at": datetime.now().isoformat(timespec="seconds"),
        "items": items,
        "instructions": (
            "For each item: fill empty translations, fix duplicate sense "
            "translations, proofread existing ones. Update progress.json + "
            "commit when done. See PLAN.md §3."
        ),
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
