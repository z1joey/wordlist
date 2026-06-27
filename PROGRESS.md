# Dictionary Completion Progress

> **→ Forward**: a.json index 4320 | **← Backward**: v.json index 1057 | **Updated**: 1782562758

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 20,630 |
| Remaining | 44,237 |
| Completion | 31.80% |
| Forward agent | a.json (4,600 / 4,900) |
| Backward agent | v.json (254 / 1,058) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).  
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.  
> Only ONE file shows `← in_progress` — the file with the backward cursor.

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,600 | ██████████████████ 94% | → in_progress |
| b.json | 3,601 | 0 | ···················· 0% | ⬜ pending |
| c.json | 6,275 | 0 | ···················· 0% | ⬜ pending |
| d.json | 3,729 | 0 | ···················· 0% | ⬜ pending |
| e.json | 2,639 | 0 | ···················· 0% | ⬜ pending |
| f.json | 2,472 | 0 | ···················· 0% | ⬜ pending |
| g.json | 1,990 | 0 | ···················· 0% | ⬜ pending |
| h.json | 2,510 | 0 | ···················· 0% | ⬜ pending |
| i.json | 2,686 | 0 | ···················· 0% | ⬜ pending |
| j.json | 482 | 0 | ···················· 0% | ⬜ pending |
| k.json | 588 | 0 | ···················· 0% | ⬜ pending |
| l.json | 2,083 | 0 | ···················· 0% | ⬜ pending |
| m.json | 3,549 | 0 | ···················· 0% | ⬜ pending |
| n.json | 1,598 | 0 | ···················· 0% | ⬜ pending |
| o.json | 1,588 | 0 | ···················· 0% | ⬜ pending |
| p.json | 5,427 | 0 | ···················· 0% | ⬜ pending |
| q.json | 293 | 0 | ···················· 0% | ⬜ pending |
| r.json | 2,889 | 0 | ···················· 0% | ⬜ pending |
| s.json | 7,019 | 0 | ···················· 0% | ⬜ pending |
| t.json | 3,227 | 0 | ···················· 0% | ⬜ pending |
| u.json | 2,578 | 0 | ···················· 0% | ⬜ pending |
| v.json | 1,058 | 254 | ██░░░░░░░░░░░░░░░░ 24% | ← in_progress |
| w.json | 1,306 | 1,306 | ███████████████████ 100% | ✅ done |
| x.json | 92 | 84 | ██████████████████ 91% | ⚠️ pending (8 empties) |
| y.json | 149 | 149 | ███████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **20,630** | **███░░░░░░░░░░░░░░░░ 31.80%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| → Forward | F-a-0173 | a.json | 4320–4344 | ⬜ pending | — |
| ← Backward | B-v-0001 | v.json | 1057–1033 | ⬜ pending | — |

## 📝 Last Batches

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| F-a-0165 to F-a-0172 | a.json | 4120–4319 | 200 | MiniMax-M2.7-highspeed | — | ✅ done |
| B-w-0050 | w.json | 80–56 | 25 | MiniMax-M2.7-highspeed | — | ✅ done |
| B-w-0051 | w.json | 55–31 | 25 | MiniMax-M2.7-highspeed | — | ✅ done |
| B-w-0052 | w.json | 30–1 | 30 | MiniMax-M2.7-highspeed | — | ✅ done |
| B-w-0053 to B-w-0057 | w.json | 633–1 | 125 | MiniMax-M2.7-highspeed | — | ✅ done |
| B-w-0058 | w.json | 633–1205 | 120 | MiniMax-M2.7-highspeed | — | ✅ done |

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
