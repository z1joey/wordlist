# Dictionary Completion Progress

> **→ Forward**: b.json index 772 | **← Backward**: u.json index 2282 | **Updated**: 1751277858

## 📊 Summary

| Metric | Count |
|--------|-------|
| Total entries | 64,867 |
| Reviewed & validated | 33,880 |
| Remaining | 32,987 |
| Completion | 52.2% |
| Forward agent | b.json (2,081 / 3,601) |
| Backward agent | u.json (1,283 / 2,578) |

## 📋 File Progress

| File | Total | Done | Bar | Status |
|------|-------|------|-----|--------|
| a.json | 4,900 | 4,900 | ███████████████████ 100% | ✅ done |
| b.json | 3,601 | 2,081 | ███████████░░░░░░░░░ 58% | → in_progress |
| c.json | 6,275 | 2,717 | ████████░░░░░░░░░░░░ 43% | ⬜ pending |
| d.json | 3,729 | 1,809 | █████████░░░░░░░░░░░ 49% | ⬜ pending |
| e.json | 2,639 | 1,276 | █████████░░░░░░░░░░░ 48% | ⬜ pending |
| f.json | 2,472 | 1,266 | ██████████░░░░░░░░░░░ 51% | ⬜ pending |
| g.json | 1,990 | 851 | ████████░░░░░░░░░░░░ 43% | ⬜ pending |
| h.json | 2,510 | 1,045 | ████████░░░░░░░░░░░░ 42% | ⬜ pending |
| i.json | 2,686 | 1,469 | ██████████░░░░░░░░░░░ 55% | ⬜ pending |
| j.json | 482 | 211 | ████████░░░░░░░░░░░░ 44% | ⬜ pending |
| k.json | 588 | 177 | ██████░░░░░░░░░░░░░░ 30% | ⬜ pending |
| l.json | 2,083 | 869 | ████████░░░░░░░░░░░░ 42% | ⬜ pending |
| m.json | 3,549 | 1,483 | ████████░░░░░░░░░░░░ 42% | ⬜ pending |
| n.json | 1,598 | 559 | ██████░░░░░░░░░░░░░░ 35% | ⬜ pending |
| o.json | 1,588 | 722 | █████████░░░░░░░░░░░ 45% | ⬜ pending |
| p.json | 5,427 | 2,323 | ████████░░░░░░░░░░░░ 43% | ⬜ pending |
| q.json | 293 | 125 | ████████░░░░░░░░░░░░ 43% | ⬜ pending |
| r.json | 2,889 | 1,512 | ██████████░░░░░░░░░░░ 52% | ⬜ pending |
| s.json | 7,019 | 3,152 | ████████░░░░░░░░░░░░ 45% | ⬜ pending |
| t.json | 3,227 | 1,373 | ████████░░░░░░░░░░░░ 43% | ⬜ pending |
| u.json | 2,578 | 1,283 | ██████████░░░░░░░░ 50% | ← in_progress |
| v.json | 1,058 | 1,058 | ███████████████████ 100% | ✅ done |
| w.json | 1,306 | 1,259 | ██████████████████░ 96% | ✅ done |
| x.json | 92 | 72 | ███████████████░░░░░ 78% | ✅ done |
| y.json | 149 | 149 | ███████████████████ 100% | ✅ done |
| z.json | 139 | 139 | ███████████████████ 100% | ✅ done |
| **Total** | **64,867** | **33,880** | **52.2%** | |

## 🔄 Current Batches

| Direction | Batch ID | File | Range | Status |
|-----------|----------|------|-------|--------|
| → Forward | F-b-0001 | b.json | 772–796 | ⬜ pending |
| ← Backward | B-u-0081 | u.json | 2281–2257 | ⬜ pending |

## 📝 Last Batch

| Batch | File | Range | Words | Worker | Validator | Status |
|-------|------|-------|-------|--------|-----------|--------|
| F-b-0001–0005 | b.json | 344–468 | 125 | (already complete) | — | ✅ already done |
| — | a.json | IPA fix | 101 | deepseek-v4-pro | deepseek-v4-pro | ✅ done |

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
