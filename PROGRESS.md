# Dictionary Completion Progress

> **→ Forward**: a.json index 4445 | **← Backward**: v.json index 932 | **Updated**: 1782565536

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 32,078 |
| Remaining | 32,789 |
| Completion | 49.45% |
| Forward agent | a.json (4,562 / 4,900) |
| Backward agent | v.json (349 / 1,058) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.
> Only ONE file shows `← in_progress` — the file with the backward cursor.

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,562 | █████████████████░ 93% | → in_progress |
| b.json | 3,601 | 1,445 | ███████░░░░░░░░░░ 40% | ⬜ pending |
| c.json | 6,275 | 2,717 | ████████░░░░░░░░░ 43% | ⬜ pending |
| d.json | 3,729 | 1,809 | █████████░░░░░░░░ 49% | ⬜ pending |
| e.json | 2,639 | 1,276 | █████████░░░░░░░░ 48% | ⬜ pending |
| f.json | 2,472 | 1,266 | █████████░░░░░░░░ 51% | ⬜ pending |
| g.json | 1,990 | 851 | ████████░░░░░░░░░ 43% | ⬜ pending |
| h.json | 2,510 | 1,045 | ███████░░░░░░░░░░ 42% | ⬜ pending |
| i.json | 2,686 | 1,469 | ██████████░░░░░░░ 55% | ⬜ pending |
| j.json | 482 | 211 | ████████░░░░░░░░░ 44% | ⬜ pending |
| k.json | 588 | 177 | █████░░░░░░░░░░░ 30% | ⬜ pending |
| l.json | 2,083 | 869 | ████████░░░░░░░░░ 42% | ⬜ pending |
| m.json | 3,549 | 1,483 | ████████░░░░░░░░░ 42% | ⬜ pending |
| n.json | 1,598 | 559 | ██████░░░░░░░░░░░ 35% | ⬜ pending |
| o.json | 1,588 | 722 | ████████░░░░░░░░░ 45% | ⬜ pending |
| p.json | 5,427 | 2,323 | ████████░░░░░░░░░ 43% | ⬜ pending |
| q.json | 293 | 125 | ████████░░░░░░░░░ 43% | ⬜ pending |
| r.json | 2,889 | 1,512 | █████████░░░░░░░░ 52% | ⬜ pending |
| s.json | 7,019 | 3,152 | ████████░░░░░░░░░ 45% | ⬜ pending |
| t.json | 3,227 | 1,372 | ████████░░░░░░░░░ 43% | ⬜ pending |
| u.json | 2,578 | 946 | ███████░░░░░░░░░░ 37% | ⬜ pending |
| v.json | 1,058 | 349 | █████░░░░░░░░░░░ 33% | ← in_progress |
| w.json | 1,306 | 1,259 | █████████████████░ 96% | ⚠️ pending (47 empties) |
| x.json | 92 | 66 | █████████████░░░░░ 72% | ⚠️ pending (26 empties) |
| y.json | 149 | 149 | ███████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **32,078** | **█████░░░░░░░░░░░░░ 49%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| → Forward | F-a-0178 | a.json | 4445–4469 | ⬜ pending | — |
| ← Backward | B-v-0011 | v.json | 932–908 | ⬜ pending | — |

## 📝 Last Batches

| Batch | File | Range | Words | Worker | Status |
|-------|------|-------|-------|--------|--------|
| F-a-0173 to F-a-0177 | a.json | 4320–4444 | 125 | MiniMax-M3 | ✅ done |
| B-v-0001 to B-v-0005 | v.json | 1057–933 | 125 | Mavis cron | ✅ done |
| B-v-0006 to B-v-0010 | v.json | 1057–933 | 125 | Mavis cron | ✅ done |

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
