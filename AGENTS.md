# AGENTS.md — Dictionary Completion Handbook

You are an AI agent working on the **wordlist** dictionary project: an English→Chinese dictionary with 64,867 entries across 26 files (`a.json` through `z.json`).

There are **two roles**, plus a **combined mode** that runs both in one session.

**Use combined mode unless you have a specific reason not to.** It eliminates handoff gaps.

---

## ⚡ Combined Mode (Recommended)

Run both worker and validator back-to-back on the same batch. No handoff, no waiting.

### Workflow

```
1. Read PROGRESS.md → find cursor
2. Create next batch (25 entries from cursor)
3. Mark batch 🟡 working in PROGRESS.md
4. Process all 25 entries (follow Working Agent workflow below)
5. Immediately audit all 25 entries (follow Validating Agent checklist below)
6. If ALL pass:
   → set provider + timestamp on all 25 entries
   → mark batch ✅ done, advance cursor
   → commit & push
7. If ANY fail:
   → fix the failing entries
   → re-audit
   → then stamp, mark done, advance cursor, commit
```

The full workflow — translate, audit, stamp, commit — should complete a 25-entry batch in ~45 minutes.

---

## 🔨 Working Agent (standalone)

Use this when splitting work across sessions. Prefer combined mode.

Your job: fill and verify every field in a batch of 25 entries. You do NOT set `metadata.provider` or `metadata.updatedAt` — the validator does.

### Quick Start

1. Read [`PROGRESS.md`](./PROGRESS.md) — find the first batch with status `⬜ pending`
2. If no pending batch exists, create the next one:
   - Follow the cursor in PROGRESS.md to find `file` and `index`
   - The batch is the next 25 entries from that cursor position
   - Batch ID format: `{file_letter}-{batch_number:04d}` (e.g., `a-0001` for a.json batch 1)
3. Update PROGRESS.md:
   - Set batch status to `🟡 working`
   - Record your provider name and start timestamp
4. Process all 25 entries one by one
5. When done, mark batch `🟠 awaiting validation` in PROGRESS.md

### Per-Word Workflow (strict sequential order)

For **each** entry, in this exact order:

```
1. READ the entry from its JSON file
2. VERIFY definition accuracy
   - Cross-reference with Cambridge / Merriam-Webster
   - Fix any factual errors

3. VERIFY/FILL pronunciation.us.ipa
   - Must be accurate US English IPA
   - Source: Cambridge Dictionary, Merriam-Webster
   - NEVER leave empty

4. VERIFY/FILL pronunciation.uk.ipa
   - Must be accurate UK English IPA
   - NEVER leave empty

5. FOR each sense:
   a. VERIFY/FILL translation
      - Idiomatic, natural Chinese (Simplified)
      - Accurate to THIS specific sense — not generic
      - NEVER leave empty
   b. FOR each example:
      - VERIFY/FILL translation
      - NEVER leave empty (if example text exists)

6. CHECK DISTINCTNESS:
   - ALL senses within this entry MUST have DISTINCT Chinese translations
   - If two senses share the same translation, differentiate them
   - Each translation must reflect the unique meaning of its English definition

7. FOR each phrase:
   - VERIFY/FILL translation
   - NEVER leave empty (if phrase text exists)

8. VERIFY tags
   - Valid tags: cet4, cet6, gre, toefl, ielts, gk, zk, ky
   - Check if the word actually belongs to that exam vocabulary list
   - Add or remove tags as needed
   - If the word has no exam association, tags = []

9. VERIFY synonyms
   - Check each synonym is a real word and genuinely synonymous
   - Remove incorrect synonyms
   - Add missing common synonyms

10. VERIFY forms (for verbs only)
    - gerund, past, pastParticiple must all be correct
    - If the word is a verb and forms are {}, fill them
    - If the word is not a verb, forms = {} is correct

11. WRITE the entry back to its JSON file
    - All fields now fully populated and verified
    - metadata.provider and metadata.updatedAt remain AS-IS
      (do NOT touch them — the validator will set them)
```

### Hard Rules

| Rule | Consequence |
|------|-------------|
| ❌ NEVER move to next word until current word is PERFECT | Data quality |
| ❌ NEVER skip a word | Research until correct |
| ❌ NEVER set `metadata.provider` | Validator sets it |
| ❌ NEVER leave empty IPA | Must fill both US & UK |
| ❌ NEVER leave empty translation | Every sense, example, phrase |
| ❌ NEVER reuse same Chinese translation across senses | Each sense must be distinct |
| ✅ ALWAYS fill every field completely before writing back | Completeness |
| ✅ ALWAYS update PROGRESS.md after the batch is done | Tracking |

### Batch Size & Timing

- **25 entries per batch** (~30 minutes)
- Some words (rare terms, technical vocabulary) will take longer — expected and acceptable

---

## 🔍 Validating Agent (standalone)

Use this when picking up a `🟠 awaiting validation` batch left by another session. Prefer combined mode.

Your job: audit a batch completed by a working agent. You are the quality gate — only you set `metadata.provider` and `metadata.updatedAt`.

### Quick Start

1. Read [`PROGRESS.md`](./PROGRESS.md) — find the first batch with status `🟠 awaiting validation`
2. Mark it `🔵 validating` and record your start time
3. Audit all 25 entries against the Completion Criteria
4. **If ALL pass:** set provider/timestamp, mark `✅ done`, advance cursor
5. **If ANY fail:** mark `❌ rejected`, note failures for working agent to fix

### Per-Entry Audit Checklist

For each entry, confirm ALL of the following. Check each one — do not skip:

```
☐ pronunciation.us.ipa
   - Non-empty
   - Accurate (cross-check Cambridge/Merriam-Webster)
   - Correct IPA notation

☐ pronunciation.uk.ipa
   - Non-empty
   - Accurate (cross-check Cambridge/Merriam-Webster)
   - Correct IPA notation

☐ Every senses[].translation
   - Non-empty
   - Accurate, idiomatic Chinese matching the English definition
   - Not a literal/mechanical translation

☐ senses[].translation DISTINCTNESS
   - NO two senses share the same Chinese translation
   - Each translation reflects its unique English definition

☐ Every senses[].examples[].translation
   - Non-empty (for each example that has text)
   - Accurate Chinese translation of the example sentence

☐ Every phrases[].translation
   - Non-empty (for each phrase that has text)
   - Accurate Chinese translation

☐ tags
   - Verified against actual exam word lists
   - No incorrect tag assignments

☐ synonyms
   - All listed words are genuine synonyms
   - No missing major synonyms

☐ forms
   - If verb: gerund, past, pastParticiple are all correct and non-empty
   - If not verb: forms is {}

☐ metadata.provider
   - Currently empty (working agent should NOT have set it)
   - If it has a value, flag for review — working agent violated rules
```

### After Audit — ALL Pass

If EVERY entry passes EVERY check:

1. For each entry:
   - SET `metadata.provider` = YOUR MODEL NAME ONLY (e.g., `"deepseek-v4-pro"`)
   - SET `metadata.updatedAt` = current Unix timestamp (integer, seconds since epoch)
   - WRITE entry back to JSON file

2. Update PROGRESS.md:
   - Mark batch `✅ done`
   - Record validator name, timestamp
   - **Advance cursor** to next unprocessed index
   - Update file progress bar and done count
   - Update summary counts

3. Commit:
   ```
   feat({batch_id}): review + validate entries {range}
   ```

### After Audit — ANY Fail

If ANY entry fails ANY check:

1. **DO NOT set provider or timestamp** on any entry — leave them as-is
2. Update PROGRESS.md:
   - Mark batch `❌ rejected`
   - Add a note under the batch row describing:
     - Which entry indices failed
     - What specific checks failed
     - Brief description of the problem
   - **Do NOT advance cursor**

3. The batch returns to `⬜ pending` implicitly — a working agent will pick it up and fix the issues

### Hard Rules

| Rule | Consequence |
|------|-------------|
| ❌ NEVER set provider on an entry with ANY issue | Data integrity |
| ❌ NEVER approve duplicate translations across senses | Quality |
| ❌ NEVER approve empty fields | Completeness |
| ❌ NEVER include agent name/hostname in provider | Model name only |
| ✅ ALWAYS verify every entry independently | No assumptions |
| ✅ ALWAYS use Unix timestamps (integer) | Consistency |

---

## 🔄 Batch Lifecycle

```
⬜ pending  →  🟡 working  →  🟠 awaiting validation  →  🔵 validating
                                                              │
                                              ┌─────────────────┤
                                              ▼                  ▼
                                         ✅ done            ❌ rejected
                                      (cursor ++)      (back to working agent)
```

---

## 📐 Data Schema

Each entry in every JSON file has this exact structure:

```json
{
  "word": "string",
  "pronunciation": {
    "us": { "ipa": "string" },
    "uk": { "ipa": "string" }
  },
  "forms": {
    "gerund": "string",
    "past": "string",
    "pastParticiple": "string"
  },
  "tags": ["string"],
  "synonyms": ["string"],
  "entries": [
    {
      "partOfSpeech": "string",
      "senses": [
        {
          "id": "string",
          "definition": "string",
          "translation": "string",
          "examples": [
            { "text": "string", "translation": "string" }
          ]
        }
      ]
    }
  ],
  "phrases": [
    { "text": "string", "translation": "string" }
  ],
  "metadata": {
    "provider": "string",
    "updatedAt": 0
  }
}
```

### Field Constraints

| Field | Required | Empty allowed? | Notes |
|-------|----------|----------------|-------|
| `word` | Yes | No | |
| `pronunciation.us.ipa` | Yes | **No** | Must be accurate IPA |
| `pronunciation.uk.ipa` | Yes | **No** | Must be accurate IPA |
| `forms` | Yes | `{}` allowed | Only fill for verbs |
| `forms.gerund` | If verb | **No** | |
| `forms.past` | If verb | **No** | |
| `forms.pastParticiple` | If verb | **No** | |
| `tags` | Yes | `[]` allowed | Verified against exam lists |
| `synonyms` | Yes | `[]` allowed | Verified for accuracy |
| `entries` | Yes | No | At least one sense |
| `senses[].definition` | Yes | No | English definition |
| `senses[].translation` | Yes | **No** | Chinese, distinct per sense |
| `senses[].examples` | Yes | `[]` allowed | |
| `senses[].examples[].text` | If example exists | No | |
| `senses[].examples[].translation` | If example exists | **No** | |
| `phrases` | Yes | `[]` allowed | |
| `phrases[].text` | If phrase exists | No | |
| `phrases[].translation` | If phrase exists | **No** | |
| `metadata.provider` | Yes (set by validator) | **No** (once done) | Model name only |
| `metadata.updatedAt` | Yes (set by validator) | **No** (once done) | Unix timestamp (integer) |

### Valid Tags

| Tag | Exam |
|-----|------|
| `cet4` | College English Test Band 4 (China) |
| `cet6` | College English Test Band 6 (China) |
| `gre` | Graduate Record Examination |
| `toefl` | Test of English as a Foreign Language |
| `ielts` | International English Language Testing System |
| `gk` | 高考 (Gaokao, college entrance exam) |
| `zk` | 中考 (Zhongkao, high school entrance exam) |
| `ky` | 考研 (postgraduate entrance exam) |

### Valid Parts of Speech

`noun`, `verb`, `adjective`, `adverb`, `preposition`, `pronoun`, `interjection`, `article`, `phrase`

---

## 📂 File Organization

```
/wordlist/
  .gitignore       # Only a-z.json, AGENTS.md, PROGRESS.md tracked
  AGENTS.md        # This file
  PROGRESS.md      # Real-time progress tracker
  a.json           # Words starting with A (4,900 entries)
  b.json           # Words starting with B (3,601 entries)
  ...              # c.json through y.json
  z.json           # Words starting with Z (139 entries)
```

---

## 🧪 Quality References

- **IPA**: [Cambridge Dictionary](https://dictionary.cambridge.org/), [Merriam-Webster](https://www.merriam-webster.com/)
- **Exam word lists**: Verify against official CET4/CET6/GRE/TOEFL/IELTS vocabulary lists
- **Translations**: Use idiomatic Simplified Chinese; prefer [Youdao](https://www.youdao.com/) or [Cambridge English-Chinese](https://dictionary.cambridge.org/dictionary/english-chinese-simplified/) as reference

---

## 🚫 Common Mistakes

1. **Same translation for different senses** — a word's senses represent different meanings; their Chinese translations MUST be different
2. **Literal/mechanical translation** — translate idiomatically, not word-for-word
3. **Missing IPA** — both US and UK IPA are required for every word
4. **Agent name in provider** — use model name only (e.g., `"deepseek-v4-pro"`), never include hostname or agent ID
5. **Wrong timestamp format** — use Unix timestamp integer (e.g., `1782460314`), not date strings
6. **Skipping hard words** — never skip; research until correct

---

## 🔬 Global Validation

Run these `jq` commands periodically to audit the entire dataset. Do this in the `/wordlist` directory.

### 1. Entries with empty IPA (US or UK)
```bash
jq '[.[] | select(.pronunciation.us.ipa == "" or .pronunciation.uk.ipa == "")] | length' *.json
```

### 2. Entries with any empty sense translation
```bash
jq '[.[] | select(.entries[].senses[].translation == "")] | length' *.json
```

### 3. Entries with any empty example translation
```bash
jq '[.[] | select(.entries[].senses[].examples[]? .translation == "")] | length' *.json
```

### 4. Entries with empty phrase translations
```bash
jq '[.[] | select(.phrases[]? .translation == "")] | length' *.json
```

### 5. Entries with empty provider
```bash
jq '[.[] | select(.metadata.provider == "")] | length' *.json
```

### 6. Entries with agent-contaminated provider
```bash
grep -r '"provider": "agent-' *.json | wc -l
```

### 7. Entries with non-integer updatedAt
```bash
jq '[.[] | select(.metadata.updatedAt | type != "number")] | length' *.json
```

### 8. Duplicate translations across senses (within same entry)
```bash
jq '[.[] | select((.entries[].senses | map(.translation) | unique | length) < (.entries[].senses | map(.translation) | length))] | length' *.json
```

Run all checks:
```bash
echo "=== Empty IPA ===" && jq '[.[] | select(.pronunciation.us.ipa == "" or .pronunciation.uk.ipa == "")] | length' *.json
echo "=== Empty sense translations ===" && jq '[.[] | select(.entries[].senses[].translation == "")] | length' *.json
echo "=== Empty example translations ===" && jq '[.[] | select(.entries[].senses[].examples[]? .translation == "")] | length' *.json
echo "=== Empty phrase translations ===" && jq '[.[] | select(.phrases[]? .translation == "")] | length' *.json
echo "=== Empty provider ===" && jq '[.[] | select(.metadata.provider == "")] | length' *.json
echo "=== Agent-contaminated providers ===" && grep -r '"provider": "agent-' *.json | wc -l
echo "=== Non-integer updatedAt ===" && jq '[.[] | select(.metadata.updatedAt | type != "number")] | length' *.json
echo "=== Duplicate sense translations ===" && jq '[.[] | select((.entries[].senses | map(.translation) | unique | length) < (.entries[].senses | map(.translation) | length))] | length' *.json
```

Goal: **zero violations across all checks** at project completion.
