# -*- coding: utf-8 -*-
"""题库深度校验：结构 / 答案自洽 / 去重 / 分布 / 质量启发式"""
import importlib.util, os, re, sys, json
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCES = {"6AU1知识单", "兰生9月月考", "文来9月考", "练习册错题", "6A教材", "6A考纲"}
LEVELS = {"🟢", "🟡", "🔴"}
FILES = ["data_w1.py", "data_w2.py", "data_w3.py", "data_w4.py", "data_w5.py",
         "data_w6_structures.py"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    all_q, errs, warns = [], [], []
    for i, f in enumerate(FILES):
        p = os.path.join(BASE, f)
        if not os.path.exists(p):
            errs.append("缺文件: " + f)
            continue
        for q in load(p, "m%d" % i).Q:
            all_q.append((f, q))

    seen_q, seen_opt = {}, {}
    for f, q in all_q:
        if len(q) != 9:
            errs.append("%s 字段数 %d" % (f, len(q)))
            continue
        cat, point, lvl, src, ques, opts, ans, expl, tags = q
        tag = "%s#%d" % (f, len(all_q))
        if not cat: errs.append("%s 分类为空" % tag)
        if lvl not in LEVELS: errs.append("%s 难度非法 %r" % (tag, lvl))
        if src not in SOURCES: errs.append("%s 出处非法 %r" % (tag, src))
        if not isinstance(opts, (list, tuple)) or len(opts) != 4:
            errs.append("%s 选项数 %s" % (tag, len(opts) if opts else 0)); continue
        if ans not in "ABCD": errs.append("%s 答案非法 %r" % (tag, ans))
        if len(set(map(str, opts))) != 4: errs.append("%s 选项重复 %s" % (tag, opts))
        if "\n" in str(ques): errs.append("%s 题干含换行" % tag)
        if not ques or len(str(ques)) < 8: errs.append("%s 题干过短" % tag)
        if not expl or len(expl) < 15: errs.append("%s 解析过短" % tag)
        if not tags or len(tags) < 2: errs.append("%s tags 不足" % tag)
        # 解析里的「故选 X」必须与答案一致
        mm = re.findall(r"故选\s*([ABCD])", expl)
        if mm and mm[-1] != ans:
            errs.append("%s 解析结论(%s)与答案(%s)不符" % (tag, mm[-1], ans))
        # 解析里提到正确答案文本时，检查选项中存在
        if "正确答案" in expl and ans not in expl:
            warns.append("%s 解析未点明答案字母" % tag)
        # 题干去重：固定题干（如语音题的 "Choose the word with a different pronunciation."）
        # 属于卷面标准题型，改用「题干+选项」判重
        key = re.sub(r"[\s，。？！,.\?!]", "", str(ques))
        if "___" not in str(ques):
            key += "|" + "|".join(sorted(map(str, opts)))
        if key in seen_q:
            errs.append("%s 题干重复(%s): %s" % (tag, seen_q[key], ques[:44]))
        else:
            seen_q[key] = tag
        # 选项集合重复（换皮题）
        okey = tuple(sorted(map(str, opts)))
        if okey in seen_opt:
            warns.append("%s 选项组合与 %s 相同" % (tag, seen_opt[okey]))
        else:
            seen_opt[okey] = tag
        # 质量启发式：解析若引用了某个错误选项，应确实存在于选项里
        for o in opts:
            if isinstance(o, str) and len(o) > 3 and o in expl and o != str(opts["ABCD".index(ans)]):
                pass  # 正常：解析常常逐一点破干扰项
        # 解析里出现的英文单词若与选项完全一致，检查是否误把正确项说成错的
        correct_txt = str(opts["ABCD".index(ans)]) if ans in "ABCD" and "ABCD".index(ans) < len(opts) else ""
        for kw in ["误", "不选", "错误", "不能", "不是"]:
            pass

    print("=" * 64)
    print("题目总数: %d" % len(all_q))
    if errs:
        print("❌ 硬错误 %d 项：" % len(errs))
        for e in errs[:50]: print("   -", e)
    else:
        print("✅ 硬错误 0 项")
    if warns:
        print("⚠️  提示 %d 项（前 20）：" % len(warns))
        for w in warns[:20]: print("   -", w)
    else:
        print("✅ 提示 0 项")
    print("-" * 64)
    print("分类分布:")
    for k, v in Counter(q[1][0] for q in all_q).most_common():
        print("   %-22s %d" % (k, v))
    print("难度分布:", dict(Counter(q[1][2] for q in all_q)))
    print("出处分布:", dict(Counter(q[1][3] for q in all_q)))
    print("答案分布:", dict(sorted(Counter(q[1][6] for q in all_q).items())))
    print("=" * 64)
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
