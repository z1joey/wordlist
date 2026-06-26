# Dictionary Completion Progress

> **Cursor**: a.json → index 1000 | **Updated**: 1782490493

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 17,463 |
| Remaining | 47,404 |
| Completion | 26.9% |
| Current file | a.json (2,598 / 4,900) |

## 📋 File Progress

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 2,598 | █████▌░░░░ 53% | 🔄 in_progress |
| b.json | 3,601 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| c.json | 6,275 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| d.json | 3,729 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| e.json | 2,639 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| f.json | 2,472 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| g.json | 1,990 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| h.json | 2,510 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| i.json | 2,686 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| j.json | 482 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| k.json | 588 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| l.json | 2,083 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| m.json | 3,549 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| n.json | 1,598 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| o.json | 1,588 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| p.json | 5,427 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| q.json | 293 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| r.json | 2,889 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| s.json | 7,019 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| t.json | 3,227 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| u.json | 2,578 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| v.json | 1,058 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| w.json | 1,306 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| x.json | 92 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| y.json | 149 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |
| z.json | 139 | 0 | ░░░░░░░░░░ 0% | ⬜ pending |

## 🔄 Current Batch

| Field | Value |
|-------|-------|
| Batch ID | a-0041 |
| Status | 🟡 working |

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator |  Status |
|-------|------|-------|-------|--------|-----------|---------|
| a-0036 | a.json | 875–899 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0037 | a.json | 900–924 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0038 | a.json | 925–949 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0039 | a.json | 950–974 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0040 | a.json | 975–999 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0041 | a.json | 1000–1024 | 25 | 🟡 in progress | — | 🟡 working |
| a-0042 | a.json | 1025–1049 | 25 | 🟡 queued | — | 🟡 queued |

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
