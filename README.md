# 六年级英语每日刷题 v2 —— 源文件说明

本目录是《六年级英语每日刷题 v2》的**可复现构建源**，输出文件为：
`../六年级英语每日刷题_v2.html`（纯静态单文件，双击即可用，无需联网）。

## 文件一览

| 文件 | 作用 |
|---|---|
| `_SPEC.md` | 出题规范：字段定义、质量红线、验收标准 |
| `build.py` | 构建脚本：合并数据 → 校验 → 注入模板 → 输出 HTML |
| `validate.py` | 深度校验：结构、答案自洽、题干去重、分布统计 |
| `gen_structures.py` | 由 `../词型结构_源文件/verb_structures.py` 自动生成词型结构类题目 |
| `data_w1.py` | 语音·元音 / 语音·辅音与重音 / 词形转换 / 名词与数词（48 题） |
| `data_w2.py` | 一般现在时 / 现在进行时 / 一般过去时 / 一般将来时 / 情态动词（45 题） |
| `data_w3.py` | 介词 / 代词 / 冠词 / There be / 祈使句 / 主谓一致 / 连词（66 题） |
| `data_w4.py` | 疑问词 / 句型转换 / 比较级 / 复合形容词 / 时间与频率 / 句子成分（55 题） |
| `data_w5.py` | 6AU1 词汇与情景 / 动词搭配 / 双宾语 / 综合运用（51 题） |
| `data_w6_structures.py` | 词型结构 11 组自动生成（54 题）——**由脚本生成，勿手改** |
| `data_knowledge.py` | 知识点讲解库（29 类 / 100+ 条） |

## 重新构建

```bash
cd "/Users/ryanpan/Desktop/AI Project/英文/每日刷题_源文件"
python3 gen_structures.py   # 重新生成词型结构题（改了 verb_structures.py 才需要）
python3 validate.py         # 深度校验，任何硬错误都会在这里报出来
python3 build.py            # 合并并输出 ../六年级英语每日刷题_v2.html
```

`build.py` 内置严格校验：**任一硬错误（字段缺失、选项不足 4 个、答案不在 ABCD、
题干重复、解析与答案不一致）都会中止构建并打印明细**，不会产出坏文件。

## 题目字段

```python
(category, point, level, source, question, options, answer, explanation, tags)
```

- `category` —— 考点分类，顺序由 `build.py` 的 `CAT_ORDER` 控制
- `level` —— 🟢 6A 必会 / 🟡 常见易错 / 🔴 偏难拔高
- `source` —— 6AU1知识单 / 兰生9月月考 / 文来9月考 / 练习册错题 / 6A教材 / 6A考纲
- `explanation` —— 中文解析，可用 `<strong>` `<em>` 强调

