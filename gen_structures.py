# -*- coding: utf-8 -*-
"""
由 词型结构_源文件/verb_structures.py（11 组 276 条）自动生成「词型结构」类题目。
规则：每题 4 选项；目标项的中文释义在 4 个选项中唯一；同组内抽干扰项。
"""
import importlib.util, random, os

BASE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location(
    "vs", os.path.join(BASE, "..", "词型结构_源文件", "verb_structures.py"))
vs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(vs)

# 组 -> (分类名, 出题条数, 方向分配)
#   方向 "cn"：题干给中文，选英文结构；"en"：题干给英文，选中文释义
PLAN = [
    ("G1",  "词型结构·to do",   6, ["cn", "cn", "en", "en", "cn", "en"]),
    ("G2",  "词型结构·doing",   6, ["cn", "en", "cn", "en", "cn", "en"]),
    ("G3",  "词型结构·to do 与 doing", 4, ["cn", "en", "cn", "en"]),
    ("G4",  "词型结构·宾语+动词原形", 3, ["cn", "en", "cn"]),
    ("G5",  "词型结构·be 动词", 6, ["cn", "en", "cn", "en", "cn", "en"]),
    ("G6",  "词型结构·动词+up", 7, ["cn", "en", "cn", "en", "cn", "en", "cn"]),
    ("G7",  "词型结构·动词+down", 5, ["cn", "en", "cn", "en", "cn"]),
    ("G8",  "词型结构·动词+out", 4, ["cn", "en", "cn", "en"]),
    ("G9",  "词型结构·动词+off", 5, ["cn", "cn", "en", "cn", "en"]),
    ("G10", "词型结构·give 短语", 4, ["cn", "en", "cn", "en"]),
    ("G11", "词型结构·go 短语", 4, ["cn", "en", "cn", "en"]),
]

CN2EN = {("G%d" % (i + 1)): g[1] for i, g in enumerate(vs.GROUPS)}
NOTE = {("G%d" % (i + 1)): g[3].replace("\n", " ") for i, g in enumerate(vs.GROUPS)}
SOURCE = {"G1": "6A教材", "G2": "6A教材", "G3": "6A教材", "G4": "6A教材", "G5": "6A教材",
          "G6": "6A考纲", "G7": "6A考纲", "G8": "6A考纲", "G9": "6A考纲",
          "G10": "6A考纲", "G11": "6A考纲"}


def usable(entries):
    """去掉占位条目、去掉中文释义重复的结构，优先 6A 难度。"""
    out, seen_cn = [], set()
    for e in entries:
        num, struct, cn, en, encn, lv, note = e
        if struct == "—" or cn == "—" or "未拍到" in cn:
            continue
        if lv == "🔴":
            continue
        if cn in seen_cn:
            continue
        seen_cn.add(cn)
        out.append(e)
    return out


def build():
    rng = random.Random(20261107)
    out_list = []
    used_cn = set()
    for gname, cat, n, dirs in PLAN:
        pool = usable(getattr(vs, gname))
        picked = []
        for e in pool:
            if len(picked) >= n:
                break
            if e[2] in used_cn:
                continue
            picked.append(e)
        for e, direction in zip(picked, dirs):
            struct, cn, en, encn, lv = e[1], e[2], e[3], e[4], e[5]
            # 干扰项：同组、结构不同、中文释义不同
            cands = [x for x in pool if x[1] != struct and x[2] != cn]
            rng.shuffle(cands)
            distract, used_vals = [], set()
            for x in cands:
                v = x[2] if direction == "cn" else x[1]
                if v in used_vals:
                    continue
                used_vals.add(v)
                distract.append(x)
                if len(distract) == 3:
                    break
            if len(distract) < 3:
                continue
            if direction == "cn":
                opts_txt = [cn] + [d[2] for d in distract]
                correct_txt = cn
            else:
                opts_txt = [struct] + [d[1] for d in distract]
                correct_txt = struct
            rng.shuffle(opts_txt)
            ai = opts_txt.index(correct_txt)
            answer = "ABCD"[ai]
            if direction == "cn":
                question = "「%s」对应的英文结构是：" % cn
                expl = ("「%s」对应 <strong>%s</strong>。%s。例：%s（%s）"
                        % (cn, struct, NOTE[gname], en, encn))
                tags = [cat.split("·")[-1], struct.split()[0]]
            else:
                question = "%s 的意思是：" % struct
                expl = ("<strong>%s</strong> 的意思是「%s」。%s。例：%s（%s）"
                        % (struct, cn, NOTE[gname], en, encn))
                tags = [cat.split("·")[-1], struct.split()[0]]
            out_list.append((cat, struct, lv, SOURCE[gname], question,
                             opts_txt, answer, expl, tags))
            used_cn.add(cn)
    return out_list


QUESTIONS = build()

if __name__ == "__main__":
    questions = QUESTIONS
    out = os.path.join(BASE, "data_w6_structures.py")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n# 由 verb_structures.py（11 组 276 条）自动生成\n")
        f.write("Q = [\n")
        for q in questions:
            f.write("    (%r,\n     %r,\n     %r,\n     %r,\n     %r,\n     %r,\n     %r,\n     %r,\n     %r),\n"
                    % q)
        f.write("]\n")
    print("生成", len(questions), "题 ->", out)
    from collections import Counter
    for k, v in Counter(q[0] for q in questions).items():
        print("  ", k, v)
    print("答案分布:", Counter(q[6] for q in questions))
