# Dictionary Completion Progress

> **→ Forward**: b.json index 772 | **← Backward**: u.json index 2274 | **Updated**: 1751214277

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 10,075 |
| Remaining | 54,792 |
| Completion | 15.5% |
| Forward agent | b.json (1,698 / 3,601) |
| Backward agent | u.json (733 / 2,578) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).  
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.  
> **🚨 Never start the next file until every entry in the current file is complete.**

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,900 | ███████████████████ 100% | ✅ done |
| b.json | 3,601 | 1,698 | ██████████░░░░░░░░ 47% | → in_progress |
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
| u.json | 2,578 | 733 | █████░░░░░░░░░░░░ 28% | ← in_progress |
| v.json | 1,058 | 1,058 | ███████████████████ 100% | ✅ done |
| w.json | 1,306 | 1,306 | ███████████████████ 100% | ✅ done |
| x.json | 92 | 92 | ███████████████████ 100% | ✅ done |
| y.json | 149 | 149 | ███████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **10,075** | **15.5%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| → Forward | F-b-0030 | b.json | 772–796 | ⬜ pending | — |
| ← Backward | B-u-0062–0066 | u.json | 2406–2274 | ✅ done | — |

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| — | a.json | final entries | 20 | deepseek-v4-pro | deepseek-v4-pro | ✅ done |

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
