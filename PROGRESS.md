# Dictionary Completion Progress

> **→ Forward**: a.json index 4570 | **← Backward**: u.json index 2577 | **Updated**: 1782568800

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 9,735 |
| Remaining | 55,132 |
| Completion | 15.0% |
| Forward agent | a.json (4,784 / 4,900) |
| Backward agent | u.json (414 / 2,578) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).  
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.  
> **🚨 Never start the next file until every entry in the current file is complete.**

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,784 | █████████████████ 98% | → in_progress |
| b.json | 3,601 | 1,450 | ████████░░░░░░░░░░ 40% | ⬜ pending (a.json not finished) |
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
| u.json | 2,578 | 414 | ███░░░░░░░░░░░░░░ 16% | ← in_progress |
| v.json | 1,058 | 1,058 | ███████████████████ 100% | ✅ done |
| w.json | 1,306 | 1,306 | ███████████████████ 100% | ✅ done |
| x.json | 92 | 92 | ███████████████████ 100% | ✅ done |
| y.json | 149 | 149 | ███████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **9,585** | **14.8%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| → Forward | F-a-0183 | a.json | 4570–4594 | ⬜ pending | — |
| ← Backward | B-u-0001 | u.json | 2577–2553 | ⬜ pending | — |

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| F-a-0182 | a.json | 4545–4569 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| B-v-0057 | v.json | 255–231 | 25 | mavis-cron | — | ✅ done |
| B-v-0058 | v.json | 230–206 | 25 | mavis-cron | — | ✅ done |
| B-v-0059 | v.json | 205–181 | 25 | mavis-cron | — | ✅ done |
| B-v-0060 | v.json | 180–156 | 25 | mavis-cron | — | ✅ done |
| B-v-0061 | v.json | 155–131 | 25 | mavis-cron | — | ✅ done |

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
