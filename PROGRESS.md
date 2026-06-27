# Dictionary Completion Progress

> **→ Forward**: a.json in_progress | **← Backward**: w.json index 430 | **Updated**: 1782555072

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 20,065 |
| Remaining | 44,802 |
| Completion | 30.93% |
| Forward agent | a.json (4,467 / 4,900) |
| Backward agent | w.json (874 / 1,306) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).  
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.  
> If both agents reach the same file, the backward agent skips to the next unprocessed file.

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,467 | ██████████████████ 91% | → in_progress |
| b.json | 3,601 | 821 | ████ 23% | → in_progress |
| c.json | 6,275 | 1,533 | ██████ 24% | → in_progress |
| d.json | 3,729 | 966 | █████ 26% | → in_progress |
| e.json | 2,639 | 722 | ███████ 27% | → in_progress |
| f.json | 2,472 | 706 | ███████ 29% | → in_progress |
| g.json | 1,990 | 454 | ██████ 23% | → in_progress |
| h.json | 2,510 | 594 | ██████ 24% | → in_progress |
| i.json | 2,686 | 700 | ██████ 26% | → in_progress |
| j.json | 482 | 125 | ███████ 26% | → in_progress |
| k.json | 588 | 96 | ████ 16% | → in_progress |
| l.json | 2,083 | 509 | █████ 24% | → in_progress |
| m.json | 3,549 | 838 | █████ 24% | → in_progress |
| n.json | 1,598 | 375 | █████ 23% | → in_progress |
| o.json | 1,588 | 387 | ██████ 24% | → in_progress |
| p.json | 5,427 | 1,295 | █████ 24% | → in_progress |
| q.json | 293 | 61 | █████ 21% | → in_progress |
| r.json | 2,889 | 880 | ██████ 30% | → in_progress |
| s.json | 7,019 | 1,798 | ██████ 26% | → in_progress |
| t.json | 3,227 | 746 | █████ 23% | → in_progress |
| u.json | 2,578 | 492 | ████ 19% | → in_progress |
| v.json | 1,058 | 254 | █████ 24% | → in_progress |
| w.json | 1,306 | 874 | ████████████ 67% | ← in_progress |
| x.json | 92 | 84 | ███████████ 91% | ← in_progress |
| y.json | 149 | 149 | ████████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ████████████████████ 100% | ✅ done |
| **Total** | **64,867** | **20,065** | **30.93%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| ← Backward | B-w-0030 to B-w-0035 | w.json | 580–431 | ✅ done | MiniMax-M2.7-highspeed |

## 📝 Last Batches

| Batch | File | Range | Words | Worker | Status |
|-------|------|-------|-------|--------|--------|
| B-w-0030 to B-w-0035 | w.json | 580–431 | 150 | MiniMax-M2.7-highspeed | ✅ done |
| B-w-0024 to B-w-0029 | w.json | 730–581 | 150 | MiniMax-M2.7-highspeed | ✅ done |
| B-w-0018 to B-w-0023 | w.json | 880–731 | 150 | MiniMax-M2.7-highspeed | ✅ done |
| B-w-0012 to B-w-0017 | w.json | 1030–881 | 150 | MiniMax-M2.7-highspeed | ✅ done |
| B-w-0006 to B-w-0011 | w.json | 1180–1031 | 150 | MiniMax-M2.7-highspeed | ✅ done |

> **Note**: Batch history may be unreliable. The cursors are derived from actual data — always trust the data files.

## 🔧 Completion Criteria (validator must confirm ALL)

- `pronunciation.us.ipa` non-empty, accurate
- `pronunciation.uk.ipa` non-empty, accurate
- All `senses[].translation` non-empty, accurate Chinese
- All `senses[].translation` are DISTINCT — no two senses share the same translation
- All `senses[].examples[].translation` non-empty, accurate (if examples exist)
- All `phrases[].translation` non-empty, accurate (if phrases exist)
- `tags` verified against word's actual exam list membership
- `synonyms` verified for accuracy
- `forms` verified (if verb: gerund, past, pastParticiple)
- `metadata.provider` = model name only
- `metadata.updatedAt` = Unix timestamp (integer)
