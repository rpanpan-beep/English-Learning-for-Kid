# 六年级英语每日刷题 v2 —— 出题规范（所有编写者必读）

## 目标用户
上海六年级学生（40+ 中年父亲陪练）。教材：**沪教牛津版 6A**（上海新教材 Unit 1–10，Unit 1 = School life 校园生活）。
出题范围必须落在 **小学六年级水平**，不超纲到初中语法。

## 输出文件格式
每个 worker 产出一个 **Python 数据文件**，只含一个顶层列表变量 `Q`，形如：

```python
# -*- coding: utf-8 -*-
# 语音 / 词形转换 / 名词数词
Q = [
    ("语音·元音", "ow 的两种读音", "🟢", "兰生9月月考",
     "Choose the word with a different pronunciation.",
     ["now", "know", "how", "cow"], "B",
     "now /naʊ/、how /haʊ/、cow /kaʊ/ 都读 /aʊ/；know /nəʊ/ 读 /əʊ/，与其他三个不同，故选 B。",
     ["ow", "元音辨音"]),
]
```

## 九个字段（顺序固定）

| # | 字段 | 说明 |
|---|------|------|
| 0 | `category` | 分类名，**必须与「分配给你的分类清单」完全一致**，一字不差 |
| 1 | `point` | 具体语法点/考点，8–16 字，如 "a/an 看音不看字" |
| 2 | `level` | 难度，只能是 `"🟢"`（6A 基础/必须会）、`"🟡"`（常见易错）、`"🔴"`（偏难/拔高） |
| 3 | `source` | 出处，只能取以下值之一：`"6AU1知识单"`、`"兰生9月月考"`、`"文来9月考"`、`"练习册错题"`、`"6A教材"`、`"6A考纲"` |
| 4 | `question` | 题干。语法填空题写完整句子，空格用 `___`；语音题写 `"Choose the word with a different pronunciation."`；选择搭配题写中文引号句 |
| 5 | `options` | **恰好 4 个**选项的 Python 列表（字符串），顺序任意，但正确答案位置要合理分布（不要全集中在同一个字母） |
| 6 | `answer` | 正确答案的字母，`"A"`/`"B"`/`"C"`/`"D"`，必须**出现在 options 的下标 0–3 内**，且与 options 顺序严格对应 |
| 7 | `explanation` | 中文解析，1–3 句。必须说明**为什么选它**，并点破干扰项错在哪。用 `<strong>` 标出关键结论 |
| 8 | `tags` | 关键词列表（2–4 个），便于搜索，如 `["冠词", "a/an"]` |

## 硬性质量要求
1. **英语必须完全正确**，符合沪教牛津 6A 的真实语感与教材例句；不要写中式英语。
2. **解析里给出的答案必须与 `answer` 字段一致**（指明"故选 X"）。
3. **解析里出现的选项字母必须自洽**：如解析写"故选 B"，则 `answer` 必须是 `"B"`。
4. 题干里 `___` 的数量必须与选项一一对应：4 个空则选项写成 `"a; an"` 这种分号分隔的组合形式。
5. **不要出现重复题**：同一个考点换皮重复出题视为不合格；同一考点最多 2–3 题且角度要不同（换语境/换干扰项）。
6. 解析里可用 `<strong>`、`<em>`；不要用 Markdown 的 `**`。
7. 中文用全角标点；题干里的英文标点保持英文半角。
8. 不要在 `question` 里放换行符（`\n`），保持单行。

## 参考语气（照这个风格写解析）
> ICT 读作 /aɪ siː tiː/，以<strong>元音音素</strong>开头，所以用 <strong>an</strong>。口诀：<em>看音不看字</em>，an hour 的 h 不发音也算元音。故选 C。

## 可用素材（只读，不要修改）
- `核验材料/兰生月考卷_提取文本.txt` —— 兰生中学 2025-2026 六上 9 月月考（解析版）全文
- `核验材料/文来月考卷_提取文本.txt` —— 文来实验 2025-2026 六上第一次考试（解析版）全文
- `核验材料/练习册错题清单_提取文本.txt` —— 孩子真实错题与错因诊断
- `核验材料/沪教牛津版6A教材知识清单_提取文本.txt` —— 6A 全册词汇/短语/语法
- `词型结构_源文件/verb_structures.py` —— 11 组 276 条词型结构（带例句、难度、中文释义）
- `../六年级英语每日刷题.html` —— 旧版 101 题，**不要照抄**，但可参考措辞风格

## 自检（交付前必须做）
写完后运行：
```bash
cd "/Users/ryanpan/Desktop/AI Project/英文/每日刷题_源文件" && python3 -c "
import importlib.util,sys
spec=importlib.util.spec_from_file_location('m','<你的文件>.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
assert all(len(q)==9 for q in m.Q), '字段数不对'
assert all(len(q[5])==4 for q in m.Q), '选项数不对'
assert all(q[6] in 'ABCD' and q[6]==chr(65+q[5].index(next(o for o in q[5] if False))) if False else q[6] in 'ABCD' for q in m.Q)
assert all(q[2] in ('🟢','🟡','🔴') for q in m.Q), '难度标记不对'
assert all(q[3] in ('6AU1知识单','兰生9月月考','文来9月考','练习册错题','6A教材','6A考纲') for q in m.Q), '来源不对'
print(len(m.Q),'题 OK')
"
```
并额外确认：`answer` 字母与 `options` 中正确项内容对应（人工抽查 5 题）。
