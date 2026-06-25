# Wordlist Dictionary Review & Improvement Plan

> **Status (live, machine-readable):** see `progress.json` in this directory.
> **Authoritative rules:** see `AGENTS.md` (sections 1, 2, 3 are the contract).
>
> This file is the **public** plan — what any agent (current or 3rd-party) needs
> to know to participate in or audit this work. Internal scratch / iteration
> logs may live elsewhere (e.g. `.mavis/`) but **the source of truth for
> "what we're doing" is this file**, and **the source of truth for "what's
> done" is `progress.json`**.

---

## 1. Mission

Review, proofread, and complete the Chinese translations in
`a.json`–`z.json`. Three things must hold for every word at the end:

1. **No duplicate sense translations within a single word** unless the English
   definitions are themselves identical (which is a data error to flag).
2. **No empty `translation` field** on any `sense`, `example`, or `phrase`
   that's reachable from a study-tagged word.
3. **Quality**: B-grade ≤ 10% per batch, C-grade = 0 (see §4).

## 2. Priority order (auto-runs through)

| Phase | What | Approx. words | Notes |
|---|---|---:|---|
| A | Tagged words (have `tags: [...]`) | 14,345 | Highest priority — these are study-list words. ~29 batches. |
| B | Untagged words that have duplicate sense translations | 681 | Fix the dupes even if the words aren't on a syllabus. ~2 batches. |
| C | Untagged words with no translations | ~50k | Fill the rest. Runs **automatically** after A + B; do not ask again. |

Tagged-first **within** a batch is determined by score:
```
score(word) = len(word['tags']) * 10    # more tags = higher study weight
            + empty_sense_count * 2     # empties first
            + duplicate_count           # dupes kill two birds
```
Sorted descending; the next 500 unseen words become the batch.

## 3. Batch pipeline (500 words per batch)

```
[SELECT]  Pick next 500 words by §2 score from the not-yet-done set.
          Worktree per batch: .worktrees/wt-<short-hash>, branch wt/<short-hash>.
          Snapshot *.bak per file before mutating.

[REVIEW]  For every sense / example / phrase in those words:
          (a) Empty? → must fill
          (b) Duplicated within the same word? → must differentiate
          (c) Existing Chinese wrong / awkward / English leak / mojibake?
              → flag for re-translation

[TRANSLATE]  Producer writes new translations; updates metadata only for
             words it actually changed (AGENTS.md §3: 改了再标).

[VERIFY]  Independent verifier scores each change A/B/C:
          - A: PASS
          - B: counted in batch's B-rate
          - C: FAIL (wrong meaning, English-only, mojibake, or duplicate
             within the same word)
          B-rate ≤ 10% per batch. C-rate = 0. On FAIL, producer retries
          ONLY the failing items (max 2 retries per batch).

[COMMIT]  One commit per batch. Merge wt/<hash> ff into
          feature/add-translations. Update progress.json (see §6).
          Clean up the worktree.
```

## 4. Quality bar

| Grade | Verdict | Constraint |
|---|---|---|
| A | PASS | Natural Chinese, sense-specific, 1–12 CJK chars typical, no leak, fits examples |
| B | Conditional | Right meaning but awkward / generic / too long / minor leak — counted in batch B-rate |
| C | FAIL | Wrong meaning, mojibake, English-only, or duplicate of another sense in the same word — must retry |

Per batch: **B ≤ 10%, C = 0**. Above that, retry the B/C items.

## 5. Out of scope (do not touch)

- `.reasonix/`, `.trae/`, `.git/` — never modify
- Adding new words, deleting words, renumbering `sense.id`
- Schema changes (current v1 in AGENTS.md §2 is the contract)
- Existing `metadata.provider` stamps on prior-pass words — do **not**
  scrub or rewrite them just because they're not in some "active provider"
  list. The provider string is a free-form historical label.

## 6. Progress tracking

**`progress.json` is the source of truth for status.** Every agent
that touches this repo must:

1. **Before starting work**: read `progress.json` to find the next
   uncompleted batch.
2. **After committing a batch**: update `progress.json` with the new
   batch entry AND increment the cumulative counters at the top.

Schema (see `progress.json` itself for the live example):
```json
{
  "schema_version": 1,
  "last_updated": "YYYY-MM-DD",
  "next_batch_id": 17,
  "totals": {
    "tagged_words_done": 0,
    "untagged_words_done": 0,
    "senses_filled": 0,
    "senses_fixed_duplicate": 0,
    "examples_filled": 0,
    "phrases_filled": 0
  },
  "batches": [
    {
      "id": 1,
      "phase": "A",
      "started_at": "YYYY-MM-DD",
      "committed_at": "YYYY-MM-DD",
      "status": "in_progress" | "committed" | "failed",
      "files": ["a.json", "b.json"],
      "word_indices": { "a.json": [0, 1, 2, ...] },
      "stats": {
        "senses_filled": 0,
        "senses_fixed_duplicate": 0,
        "examples_filled": 0,
        "phrases_filled": 0,
        "B_count": 0,
        "C_count": 0
      },
      "commit_sha": "abc1234..." | null
    }
  ]
}
```

**Why JSON and not just a markdown table?**
- LLMs can read JSON, but `jq` / Python / any tool can also read it
  deterministically.
- The next batch can be computed: `batches[-1].id + 1` or use
  `next_batch_id`.
- The score-based next-batch picker reads `progress.json` to know
  which `(file, index)` pairs are already done, so it doesn't re-pick
  completed words.

## 7. The "duplicate translation" rule in detail

The user explicitly called this out as a primary quality concern.
Enforcement:

> **Within a single word, no two `sense.translation` strings may be
> identical** — unless their English `definition` strings are also
> identical, in which case that's a data error and should be flagged
> in `progress.json.batches[].stats.flags`, not silently merged.

Same rule applies to `examples[]` within a single `sense`, and
across `sense` vs `phrases` for the same word (less critical, but
worth noting).

How to disambiguate during translate:
- Different POS → keep one, reword the other (e.g. noun 记录 vs verb 记录 → 录音/记载)
- Active vs passive → differentiate (吸收 vs 被吸收)
- General vs domain-specific → differentiate (计算 in math vs 计算机 sense)
- Otherwise → look at examples to pick sense-specific glosses

## 8. For new agents joining mid-stream

If you (an agent) just opened this repo:
1. Read `AGENTS.md` end-to-end.
2. Read `PLAN.md` (this file).
3. Run `cat progress.json | python3 -m json.tool` to see current state.
4. The first `batches` entry with `status != "committed"` is where
   to resume, OR if all batches are committed, the next batch is
   `next_batch_id`.
5. Pick the next 500 words per §2's score function, excluding any
   `(file, index)` already in a committed batch.
6. Follow §3's pipeline. Don't re-invent the verifier — copy the
   structure from `.mavis/plans/gk-fix-leftover.yaml` if available.

## 9. Reference

- Schema: `AGENTS.md` §2
- 改了再标 (changed-then-stamped) rule: `AGENTS.md` §3
- Provider free-form: `AGENTS.md` §4
- Quality baseline: `AGENTS.md` §5
- Per-file stats helper: `scripts/audit_translations.py` (only catches
  a small known-bad pattern list — not a substitute for the verifier)
- Internal iteration / reports: `.mavis/plans/` (gitignored, optional)
