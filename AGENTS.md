# AGENTS.md — wordlist 字典数据库协作规则

> 本文件供参与 wordlist 字典数据库维护的 AI agent 阅读。
> 任何 agent 修改本仓库内的 JSON 数据前，**必须**先读本文件。

---

## 1. 仓库结构

```
wordlist/
├── a.json ~ z.json          # 主数据（按首字母拆分，**唯一**的字典数据源）
├── scripts/                  # 数据处理脚本（独立维护）
├── .reasonix/                # 第三方工具数据（**不修改**、不参与字典）
├── .trae/                    # IDE 配置（**不修改**）
├── *.py, *.md, *.txt         # 审计/翻译/报告产物（中间文件，可 .gitignore）
└── u.json.bak                # u.json 修复前的备份（仅 u.json 有此文件）
```

**只允许修改 `a.json` ~ `z.json` 这 26 个文件的数据内容。**
**其它文件/文件夹一律只读。** （即便用户明确要求，也请先确认是否真的会破坏工具链。）

---

## 2. 数据 Schema（v1）

```json
{
  "word": "example",
  "pronunciation": { "us": {"ipa": ""}, "uk": {"ipa": ""} },
  "forms": {},
  "tags": ["cet4", "cet6"],
  "synonyms": [],
  "entries": [
    {
      "partOfSpeech": "noun",
      "senses": [
        {
          "id": "example-noun-1",
          "definition": "...",
          "translation": "...",        // ← EN→ZH 翻译，目标字段
          "examples": [
            { "text": "...", "translation": "..." }
          ]
        }
      ]
    }
  ],
  "phrases": [],
  "metadata": {
    "provider": "MiniMax-M3",           // ← 由本 agent 维护
    "updatedAt": "2026-06-23"            // ← 由本 agent 维护
  }
}
```

- `sense.id` 格式：`<word>-<pos>-<N>`，N 从 1 开始连续编号（部分词可能 skip，**以 u.json 实际编号为准**）
- `metadata.provider` 填本 agent 的 model identifier（**不**是团队/组织名）

---

## 3. 核心不变量 — "改了再标，不动不标"

**铁律：只有当本 agent 实际修改了 `translation` 字段时，才能更新对应 word 的 `metadata`。**

### 3.1 判定标准

| 操作 | 是否更新 `metadata` |
|---|---|
| 给某 sense 填上非空 `translation` | ✅ 更新 `metadata.provider` + `updatedAt` |
| 修改了某 sense 的现有 `translation`（润色/纠错） | ✅ 更新 |
| 仅给 `metadata` 本身加字段、没动 `translation` | ❌ 不更新 |
| 给 example 补翻译，但 sense 主翻译没动 | ❌ sense 的 `metadata` 不更新（**但 example 自身的 metadata 应更新**） |
| 删除/重组结构、没改翻译 | ❌ 不更新 |
| 仅跑了审计/统计，没改任何数据 | ❌ 不动 |

### 3.2 实现建议

任何会写 JSON 的脚本必须遵循这个模式：

```python
# 推荐：先改 translation，再决定是否更新 metadata
for word, sense in work_items:
    old_tr = sense.get("translation", "").strip()
    new_tr = do_translate(...)
    if new_tr and new_tr != old_tr:
        sense["translation"] = new_tr
        # 只有真正改了才打 tag
        meta = entry.setdefault("metadata", {})
        meta["provider"] = AGENT_MODEL_ID  # 如 "MiniMax-M3"
        meta["updatedAt"] = TODAY_ISO
```

```python
# 禁忌：批量"加 metadata"时一锅端
for entry in data:
    entry.setdefault("metadata", {"provider": "X", "updatedAt": "..."})  # ❌
```

### 3.3 校验

每次写库前后，必须跑一次一致性检查：

```python
# 标了 provider 的 word → 必须有本 agent 实际填的非空 translation
# 翻译被改过的 sense → 所属 word 的 provider 必须是本 agent
```

这是 2026-06-23 u.json 修复时的硬约束，请后续 agent 接力时严格遵守。

---

## 4. Provider 标识 — 自由形式（2026-06-25 更新）

`metadata.provider` 是一个**自由形式的字符串**，用来记录"是谁实际翻译/修改了
这条 `translation`"。它**不**是固定的身份标识；不同 agent、不同时间、不同模型
可以使用任意字符串。

**铁律**（不变）：只有当你实际修改了 `sense.translation` / `example.translation` /
`phrase.translation` 时，才能在 `metadata` 里写 `provider` + `updatedAt`。
详见 §3 "改了再标，不动不标"。

### 4.1 推荐写法

- 用模型/agent 的可识别标识：`MiniMax-M3`、`deepseek-v4-flash`、`claude-opus`、
  `gpt-5-mini`、`MiniMax-M3-2026-06-25` 等等。
- 也允许人类/混合流程的标签：`human-curated`、`MiniMax-M3+human`、
  `deepseek-v4-flash-pass1+human-proofread`。
- 不允许：留空但写了 `updatedAt`、或者 `provider` 写了但没改过翻译。

### 4.2 实际数据中的现存 provider（截至 2026-06-25，仅供参考）

| Provider | 出现次数 | 说明 |
|---|---:|---|
| `MiniMax-M3` | 846 | 2026-06-23 起的 MiniMax M3 翻译 |
| `deepseek-v4-flash` | 14,587 | 2026-06-24 起的 deepseek-v4-flash 翻译 |
| `""`（空） | 49,434 | 尚未翻译的词条 — 正常状态 |

**不要**因为某个 provider 字符串没出现在历史里就把它的词标为 "stale"。
只要该词确实有过 `translation` 改动（§3 校验通过），任何 provider 字符串都合法。

### 4.3 新 agent 加入时

无需注册 provider 列表。直接用你想用的字符串即可。

---

## 5. 翻译质量基线（2026-06-23 审计）

- 词典共 **115,954** 个 sense、**64,867** 个 word
- **66.9% sense 无翻译**（首要问题是"缺翻"，不是"翻错"）
- 已翻译 sense 中 **92% 质量 A 级**（无空、无乱码、无英文泄漏、无过长）

| Top 5 质量最好文件 | A 级率 |
|---|---:|
| q.json | 100% |
| v.json | 98.9% |
| a.json | 98.8% |
| x.json | 98.3% |
| m.json | 96.9% |

| Bottom 5 文件 | A 级率 |
|---|---:|
| z.json | 76.0% |
| y.json | 77.8% |
| k.json | 81.1% |
| l.json | 81.8% |
| w.json | 85.1% |

**未翻译最严重**：`u.json` 82.7% 空、`z.json` 81% 空、`k.json` 78.3% 空。

**已完成**：`u.json` Top 100 高频词（按学段 tag 权重 + sense 数加权排序）100% 翻译完成（101 word, 130 sense 修复）。修复报告见 `fix_top100_report.md`。

### 5.1 2026-06-25 重测

- 词条总数 **64,867 word / 115,954 sense**（基本不变）
- 缺翻 sense: **75,348 / 115,954 = 65.0%**（与 2026-06-23 基线一致）
- **Tagged 词缺翻 38.6%**、**Untagged 词缺翻 84.3%**（priority 切分见 `.mavis/plans/dictionary-review-plan.md`）
- **重复翻译问题**：**3,959 个 word** 至少有两个 sense 用了完全相同的中文
  （其中 3,158 个是 tagged 词）。例：`abode` 两个 sense 都是 `住所`、`adjust`
  四个 adj sense 都是 `调整`。
- **总磁盘影响**：即便把全部 75,348 个空翻译都补上，整个 dict 也只多 ~1.6 MB
  （58.9 MB → 60.5 MB）。瓶颈是质量，不是容量。

---

## 6. 工作流建议

1. **修改前先读本文件 + 跑一次 `audit_translations.py`** 摸清基线
2. **修改中**：先小批量试改 10-50 条 → 校验质量 → 再放量
3. **修改后**：跑 `apply_*_fix.py` 必须包含 3.3 的校验；写回前**务必备份** (`*.bak`)
4. **provider 归属**：严格按第 3 节，谁改谁标；不要替别人代签
5. **报告留痕**：每次大批量修改（>50 sense）应产出对应 `*_report.md`

---

## 7. 不在本规则范围内

- `.reasonix/`、`.trae/`、`.git/` 等工具/系统目录 — 不要碰
- `scripts/` 下的脚本 — 可以看、可以改、但别改完忘了跑通
- 用户私有的 `add_metadata.py`、`audit_*.py` — 是过往 agent 留下的工作痕迹，可参考可清理
