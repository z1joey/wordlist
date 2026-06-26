# Dictionary Completion Progress

> **Cursor**: a.json → index 1895 | **Updated**: 1782700800

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 18,069 |
| Remaining | 46,798 |
| Completion | 27.9% |
| Current file | a.json (3,246 / 4,900) |

## 📋 File Progress

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 3,246 | ████████████████████████░░░░░░░░░░░░░ 66% | 🔄 in_progress |
| b.json | 3,601 | 821 | ████░░░░░░░░░░░░░░░ 23% | 🔄 in_progress |
| c.json | 6,275 | 1,533 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| d.json | 3,729 | 966 | █████░░░░░░░░░░░░░░ 26% | 🔄 in_progress |
| e.json | 2,639 | 722 | █████░░░░░░░░░░░░░░ 27% | 🔄 in_progress |
| f.json | 2,472 | 706 | █████░░░░░░░░░░░░░░ 29% | 🔄 in_progress |
| g.json | 1,990 | 454 | ████░░░░░░░░░░░░░░░ 23% | 🔄 in_progress |
| h.json | 2,510 | 594 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| i.json | 2,686 | 700 | █████░░░░░░░░░░░░░░ 26% | 🔄 in_progress |
| j.json | 482 | 125 | █████░░░░░░░░░░░░░░ 26% | 🔄 in_progress |
| k.json | 588 | 96 | ███░░░░░░░░░░░░░░░ 16% | 🔄 in_progress |
| l.json | 2,083 | 509 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| m.json | 3,549 | 838 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| n.json | 1,598 | 375 | ████░░░░░░░░░░░░░░░ 23% | 🔄 in_progress |
| o.json | 1,588 | 387 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| p.json | 5,427 | 1,295 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| q.json | 293 | 61 | ████░░░░░░░░░░░░░░░ 21% | 🔄 in_progress |
| r.json | 2,889 | 880 | ██████░░░░░░░░░░░░░ 30% | 🔄 in_progress |
| s.json | 7,019 | 1,798 | █████░░░░░░░░░░░░░░ 26% | 🔄 in_progress |
| t.json | 3,227 | 746 | ████░░░░░░░░░░░░░░░ 23% | 🔄 in_progress |
| u.json | 2,578 | 492 | ███░░░░░░░░░░░░░░░ 19% | 🔄 in_progress |
| v.json | 1,058 | 254 | ████░░░░░░░░░░░░░░░ 24% | 🔄 in_progress |
| w.json | 1,306 | 358 | █████░░░░░░░░░░░░░░ 27% | 🔄 in_progress |
| x.json | 92 | 55 | ████████████░░░░░░░ 60% | 🔄 in_progress |
| y.json | 149 | 39 | █████░░░░░░░░░░░░░░ 26% | 🔄 in_progress |
| z.json | 139 | 36 | █████░░░░░░░░░░░░░░ 26% | 🔄 in_progress |

## 🔄 Current Batch

| Field | Value |
|-------|-------|
| Batch ID | a-0077 |
| Status | ⬜ pending |
| Worker | — |
| Started | — |

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator |  Status |
|-------|------|-------|-------|--------|-----------|---------|
| a-0071 | a.json | 1745–1769 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0072 | a.json | 1770–1794 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0073 | a.json | 1795–1819 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0074 | a.json | 1820–1844 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0075 | a.json | 1845–1869 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |
| a-0076 | a.json | 1870–1894 | 25 | MiniMax-M2.7-highspeed | MiniMax-M2.7-highspeed | ✅ done |

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
