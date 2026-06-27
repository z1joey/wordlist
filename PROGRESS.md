# Dictionary Completion Progress

> **→ Forward**: a.json index 4120 | **← Backward**: w.json index 430 | **Updated**: 1782625500

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 5,879 |
| Remaining | 58,988 |
| Completion | 9.06% |
| Forward agent | a.json (4,492 / 4,900) |
| Backward agent | w.json (874 / 1,306) |

## 📋 File Progress

> **Two agents**: → Forward (ascending: a → z). ← Backward (descending within each file: last index → first).  
> **Rule**: Never two agents on the same file at the same time. Only update the row for files you worked on.  
> If both agents reach the same file, the backward agent skips to the next unprocessed file.

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,492 | ██████████████████ 92% | → in_progress |
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
| w.json | 1,306 | 874 | █████████████ 67% | ← in_progress |
| x.json | 92 | 84 | █████████████████ 91% | ← in_progress |
| y.json | 149 | 139 | █████████████████ 93% | ← in_progress |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **5,854** | **9.03%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status | Worker |
|-----------|----------|------|-------|--------|--------|
| → Forward | F-a-0164 | a.json | 4095–4119 | ✅ done | doubao-seed-2.0-lite |
| ← Backward | B-w-0036 | w.json | 430–405 | ⬜ pending | — |

## 📝 Last Batches

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| F-a-0164 | a.json | 4095–4119 | 25 | doubao-seed-2.0-lite | doubao-seed-2.0-lite | ✅ done |
| F-a-0163 | a.json | 4070–4094 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |

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
