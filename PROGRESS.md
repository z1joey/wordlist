# Dictionary Completion Progress

> **Cursor**: a.json → index 3895 | **Updated**: 1790000000

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 4,406 |
| Remaining | 60,461 |
| Completion | 6.79% |
| Current file | a.json (4,406 / 4,900) |

## 📋 File Progress

> **Only the current file (a.json) is being processed. Do NOT update Done counts for files that haven't been reached yet. b–z are 0.**

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,406 | ██████████████████ 90% | 🔄 in_progress |
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
| v.json | 1,058 | 0 | ···················· 0% | ⬜ pending |
| w.json | 1,306 | 0 | ···················· 0% | ⬜ pending |
| x.json | 92 | 0 | ···················· 0% | ⬜ pending |
| y.json | 149 | 0 | ···················· 0% | ⬜ pending |
| z.json | 139 | 0 | ···················· 0% | ⬜ pending |
| **Total** | **64,867** | **4,281** | **6.60%** | |

## 🔄 Current Batch

> No batch currently in progress.

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| a-0151 | a.json | 3770–3794 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0152 | a.json | 3795–3819 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0153 | a.json | 3820–3844 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0154 | a.json | 3845–3869 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0155 | a.json | 3870–3894 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |

> **Note**: Batch history may be unreliable. The cursor is derived from actual data — always trust the data files over batch history.

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
