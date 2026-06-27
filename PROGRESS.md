# Dictionary Completion Progress

> **→ Forward**: a.json index 4820 | **← Backward**: v.json index 557 | **Updated**: 1751135400

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 21,176 |
| Remaining | 43,691 |
| Completion | 32.6% |
| Forward agent | a.json (4,893 / 4,900) |
| Backward agent | v.json (624 / 1,058) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).  
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.  
> Only ONE file shows `← in_progress` — the file with the backward cursor.

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,893 | █████████████████ 99% | → in_progress |
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
| v.json | 1,058 | 624 | ███████████░░░░░ 59% | ← in_progress |
| w.json | 1,306 | 1,306 | ███████████████████ 100% | ✅ done |
| x.json | 92 | 92 | ███████████████████ 100% | ✅ done |
| y.json | 149 | 149 | ███████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **7,106** | **11.0%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| → Forward | F-a-0193 | a.json | 4820–4844 | ⬜ pending | — |
| ← Backward | B-v-0026 | v.json | 557–533 | ⬜ pending | — |

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| F-a-0188 | a.json | 4695–4719 | 25 | mavis-cron | mavis-cron | ✅ done |
| F-a-0189 | a.json | 4720–4744 | 25 | mavis-cron | mavis-cron | ✅ done |
| F-a-0190 | a.json | 4745–4769 | 25 | mavis-cron | mavis-cron | ✅ done |
| F-a-0191 | a.json | 4770–4794 | 25 | mavis-cron | mavis-cron | ✅ done |
| F-a-0192 | a.json | 4795–4819 | 25 | mavis-cron | mavis-cron | ✅ done |
| B-v-0016 | v.json | 807–783 | 25 | MiniMax-M3 | — | ✅ done |
| B-v-0021 | v.json | 682–658 | 25 | mavis-cron | mavis-cron | ✅ done |
| B-v-0022 | v.json | 657–633 | 25 | mavis-cron | mavis-cron | ✅ done |
| B-v-0023 | v.json | 632–608 | 25 | mavis-cron | mavis-cron | ✅ done |
| B-v-0024 | v.json | 607–583 | 25 | mavis-cron | mavis-cron | ✅ done |
| B-v-0025 | v.json | 582–558 | 25 | mavis-cron | mavis-cron | ✅ done |

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
