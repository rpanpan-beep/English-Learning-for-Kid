# -*- coding: utf-8 -*-
"""
六年级英语每日刷题 v2 —— 构建脚本
数据来源：data_w1..w6_*.py + data_knowledge.py
输出：../六年级英语每日刷题_v2.html
"""
import importlib.util, json, os, re, sys, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
ENG = os.path.dirname(BASE)
OLD = os.path.join(ENG, "六年级英语每日刷题.html")
OUT = os.path.join(ENG, "六年级英语每日刷题_v2.html")

DATA_FILES = [
    "data_w1.py", "data_w2.py", "data_w3.py", "data_w4.py", "data_w5.py",
    "data_w6_structures.py",
]
CAT_ORDER = [
    "语音·元音", "语音·辅音与重音", "词形转换", "名词与数词",
    "冠词", "代词", "介词",
    "时态·一般现在时", "时态·现在进行时", "时态·一般过去时", "时态·一般将来时",
    "情态动词", "There be", "祈使句", "主谓一致", "连词",
    "疑问词", "句型转换", "形容词比较级", "复合形容词",
    "词型结构·to do", "词型结构·doing", "词型结构·to do 与 doing",
    "词型结构·宾语+动词原形", "词型结构·be 动词", "词型结构·动词+up",
    "词型结构·动词+down", "词型结构·动词+out", "词型结构·动词+off",
    "词型结构·give 短语", "词型结构·go 短语",
    "双宾语", "动词搭配", "6AU1词汇与情景", "时间与频率", "句子成分与句型",
    "综合运用",
]
SOURCES = ["6AU1知识单", "兰生9月月考", "文来9月考", "练习册错题", "6A教材", "6A考纲"]
LEVELS = ["🟢", "🟡", "🔴"]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    errs = []
    questions = []
    for i, f in enumerate(DATA_FILES):
        p = os.path.join(BASE, f)
        if not os.path.exists(p):
            errs.append("缺文件: " + f)
            continue
        mod = load(p, "m%d" % i)
        for q in mod.Q:
            questions.append(tuple(q))

    # ---------- 校验 ----------
    for n, q in enumerate(questions, 1):
        if len(q) != 9:
            errs.append("#%d 字段数 %d" % (n, len(q)))
            continue
        cat, point, lvl, src, question, opts, ans, expl, tags = q
        if cat not in CAT_ORDER:
            errs.append("#%d 未知分类 %s" % (n, cat))
        if lvl not in LEVELS:
            errs.append("#%d 难度非法 %s" % (n, lvl))
        if src not in SOURCES:
            errs.append("#%d 来源非法 %s" % (n, src))
        if not isinstance(opts, (list, tuple)) or len(opts) != 4:
            errs.append("#%d 选项数 %s" % (n, len(opts) if opts else 0))
            continue
        if ans not in ("A", "B", "C", "D"):
            errs.append("#%d 答案非法 %s" % (n, ans))
        if "\n" in str(question):
            errs.append("#%d 题干含换行" % n)
        if not expl or len(expl) < 10:
            errs.append("#%d 解析过短" % n)
        if len(set(opts)) != 4:
            errs.append("#%d 选项重复: %s" % (n, opts))

    # 题干去重：固定题干（语音题标准句）属于卷面固定题型，按「题干+选项」判重
    seen_q = {}
    for n, q in enumerate(questions, 1):
        key = re.sub(r"\s+", "", q[4])
        if "___" not in str(q[4]):
            key += "|" + "|".join(sorted(map(str, q[5])))
        if key in seen_q:
            errs.append("#%d 题干与 #%d 重复: %s" % (n, seen_q[key], q[4][:40]))
        else:
            seen_q[key] = n

    # ---------- 知识点 ----------
    kmod = load(os.path.join(BASE, "data_knowledge.py"), "km")
    knowledge = kmod.K
    for k in knowledge:
        if set(k.keys()) != {"category", "icon", "level", "points"}:
            errs.append("知识点 %s 字段集不对" % k.get("category"))
        for pt in k.get("points", []):
            need = {"name", "rule", "examples", "warn", "tip"}
            if set(pt.keys()) != need:
                errs.append("知识点 %s / %s 字段集不对: %s" % (k["category"], pt.get("name"), sorted(pt.keys())))

    if errs:
        print("=== 校验未通过（%d 项）===" % len(errs))
        for e in errs[:60]:
            print("  -", e)
        sys.exit(1)

    # ---------- 排序与编号 ----------
    def ckey(c):
        return CAT_ORDER.index(c) if c in CAT_ORDER else 999
    questions.sort(key=lambda q: (ckey(q[0]), q[1]))
    out_q = []
    for i, q in enumerate(questions, 1):
        cat, point, lvl, src, question, opts, ans, expl, tags = q
        out_q.append({
            "id": i, "category": cat, "point": point, "level": lvl, "source": src,
            "question": question, "options": list(opts), "answer": ans,
            "explanation": expl, "tags": list(tags),
        })

    cats = {}
    for q in out_q:
        cats[q["category"]] = cats.get(q["category"], 0) + 1
    srcs = {}
    for q in out_q:
        srcs[q["source"]] = srcs.get(q["source"], 0) + 1
    lvls = {}
    for q in out_q:
        lvls[q["level"]] = lvls.get(q["level"], 0) + 1

    # ---------- CSS：从旧版提取并追加 ----------
    old = open(OLD, encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", old, re.S).group(1)
    css += EXTRA_CSS

    today = datetime.date.today().isoformat()
    html = TEMPLATE
    html = html.replace("/*__CSS__*/", css)
    html = html.replace("__QUESTIONS__", json.dumps(out_q, ensure_ascii=False))
    html = html.replace("__KNOWLEDGE__", json.dumps(knowledge, ensure_ascii=False))
    html = html.replace("__CATLIST__", json.dumps(cats, ensure_ascii=False))
    html = html.replace("__CATLIST_CNT__", str(len(cats)))
    html = html.replace("__KPCNT__", str(sum(len(k["points"]) for k in knowledge)))
    html = html.replace("__SRCLIST__", json.dumps(srcs, ensure_ascii=False))
    html = html.replace("__LVLLIST__", json.dumps(lvls, ensure_ascii=False))
    html = html.replace("__BUILD_DATE__", today)
    html = html.replace("__TOTAL__", str(len(out_q)))
    html = html.replace("__PRINT_TITLE__", "综合练习")
    html = html.replace("__PRINT_N__", "0")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ 生成:", OUT)
    print("   题目 %d 道 | 分类 %d 类 | 知识点 %d 类 / %d 条 | %s"
          % (len(out_q), len(cats), len(knowledge),
             sum(len(k["points"]) for k in knowledge), today))
    print("   难度:", lvls)
    print("   出处:", srcs)


EXTRA_CSS = """
  /* ===== v2 新增 ===== */
  /* 修复：页眉改为非吸顶，导航单独吸顶，避免滚动后导航被页眉遮挡而点不动 */
  header { position: relative; z-index: 100; }
  nav { position: sticky; top: 0; z-index: 99; }
  .q-meta { display:flex; gap:6px; align-items:center; flex-wrap:wrap; }
  .badge { font-size:11px; padding:2px 8px; border-radius:10px; font-weight:600; white-space:nowrap; }
  .badge.lv-🟢 { background:#E8F5E9; color:#2E7D32; }
  .badge.lv-🟡 { background:#FFF4E0; color:#EF6C00; }
  .badge.lv-🔴 { background:#FFEBEE; color:#C62828; }
  .badge.src { background:#EEF3FC; color:#4F8EF7; }
  .chip-count { opacity:.55; margin-left:5px; font-size:11px; }
  .quick-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:10px; margin-bottom:18px; }
  .quick-card {
    background:white; border:1.5px solid var(--border); border-radius:12px; padding:14px 12px;
    text-align:center; cursor:pointer; transition:all .18s; box-shadow:var(--shadow);
  }
  .quick-card:hover { border-color:var(--primary); transform:translateY(-2px); box-shadow:var(--shadow-lg); }
  .quick-card .ico { font-size:24px; }
  .quick-card .t { font-weight:600; font-size:14px; margin-top:4px; }
  .quick-card .s { font-size:12px; color:var(--text-light); margin-top:2px; }
  .filter-row { display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-bottom:12px; }
  .filter-row label { font-size:13px; color:var(--text-light); font-weight:600; }
  .filter-row .category-list { display:flex; flex-wrap:wrap; gap:6px; }
  #setup-preview { margin-top:12px; font-size:13px; color:var(--text-light); background:#F5F8FF; padding:10px 14px; border-radius:8px; border:1px solid #E1E8F0; }
  select.pick { padding:8px 12px; border-radius:6px; border:1px solid var(--border); font-size:14px; background:white; }
  .kp-head { display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
  .kp-warn { background:#FFF4E0; border-left:3px solid #FFB347; padding:8px 10px; margin:6px 0; border-radius:0 6px 6px 0; font-size:13px; color:#8a5a00; }
  .kp-tip { background:#EAF3FF; border-left:3px solid var(--primary); padding:8px 10px; margin:6px 0; border-radius:0 6px 6px 0; font-size:13px; color:#1f4e79; }
  .print-only { display:none; }
  @media print {
    header, nav, .btn, .quick-grid, .reset-btn, #practice-setup, .no-print { display:none !important; }
    body { background:#fff; }
    .view { display:none !important; }
    .view.active { display:block !important; }
    .card, .question-card { box-shadow:none; border:1px solid #ccc; page-break-inside:avoid; }
    .question-card { border-left:1px solid #ccc; }
    .q-option { padding:4px 8px; }
    .print-only { display:block; }
    .q-explanation { display:none !important; }
    .q-tag, .badge { display:none !important; }
    #print-header { display:block; text-align:center; margin-bottom:14px; font-size:15px; font-weight:700; }
    #print-header .sub { font-size:11px; font-weight:400; color:#666; margin-top:4px; }
  }
"""


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🌟 六年级英语每日刷题 v2</title>
<style>
/*__CSS__*/
</style>
</head>
<body>
<header>
  <h1>🌟 六年级英语每日刷题 <span style="font-size:13px;opacity:.85;">v2 · 全册版</span></h1>
  <div class="subtitle">沪教牛津版 6A　·　题库 __TOTAL__ 道 / __CATLIST_CNT__ 个考点　·　含兰生 9 月月考、文来 9 月考、练习册错题与 6AU1 知识单原题</div>
</header>

<nav>
  <button data-view="home" class="active">🏠 首页</button>
  <button data-view="practice">📝 每日刷题</button>
  <button data-view="knowledge">📚 知识点</button>
  <button data-view="errors">❌ 错题本</button>
  <button data-view="progress">📊 学习进度</button>
</nav>

<main>
  <!-- ============ 首页 ============ -->
  <section class="view active" id="view-home">
    <div class="stats-grid">
      <div class="stat-card"><div class="num streak" id="home-streak">0</div><div class="label">连续打卡（天）</div></div>
      <div class="stat-card"><div class="num" id="home-answered">0</div><div class="label">累计答题</div></div>
      <div class="stat-card"><div class="num" id="home-accuracy">0%</div><div class="label">正确率</div></div>
      <div class="stat-card"><div class="num" id="home-mastered">0</div><div class="label">已攻克错题</div></div>
    </div>

    <div class="card">
      <div id="storage-warn" style="display:none; background:#FFF4E0; border-left:3px solid #FFB347; padding:10px 14px; border-radius:0 8px 8px 0; margin-bottom:16px; font-size:13px; color:#8a5a00;">
        ⚠️ 当前环境无法使用本地存储（localStorage），本次答题记录与错题本<b>不会被保存</b>，刷新页面即清空。建议改用 Chrome / Edge 直接打开本文件，或部署到网址后使用。
      </div>
      <h2 style="font-size:17px; margin-bottom:14px;">🚀 快速开始</h2>
      <div class="quick-grid">
        <div class="quick-card" onclick="startSmart(10)">
          <div class="ico">🎯</div><div class="t">每日 10 题</div>
          <div class="s">错题优先 + 新题补充</div>
        </div>
        <div class="quick-card" onclick="startSmart(20)">
          <div class="ico">⚡</div><div class="t">每日 20 题</div>
          <div class="s">周末加练档</div>
        </div>
        <div class="quick-card" onclick="startWrongOnly()">
          <div class="ico">❌</div><div class="t">只做错题</div>
          <div class="s" id="qc-wrong">错题本为空</div>
        </div>
        <div class="quick-card" onclick="startRandom(15)">
          <div class="ico">🔀</div><div class="t">随机 15 题</div>
          <div class="s">跨考点随机抽</div>
        </div>
      </div>
      <input type="text" id="keyword-input" placeholder="🔍 输入语法点或短语关键词，如：冠词 / ten-minute / give / 介词" style="width:100%; padding:11px 14px; border:1.5px solid var(--border); border-radius:8px;" onkeydown="if(event.key==='Enter') searchByKeyword()" />
      <button class="btn btn-secondary" style="margin-top:10px; width:100%;" onclick="searchByKeyword()">🔍 用关键词搜索</button>
    </div>

    <div class="card">
      <h2 style="font-size:17px; margin-bottom:6px;">📂 按考点刷题</h2>
      <p style="font-size:12px; color:var(--text-light); margin-bottom:12px;">点击考点进入设置页，可再选题量。括号内为该考点题量。</p>
      <div class="category-list" id="home-categories"></div>
    </div>
  </section>

  <!-- ============ 刷题 ============ -->
  <section class="view" id="view-practice">
    <div id="practice-setup">
      <div class="card">
        <h2 style="font-size:17px; margin-bottom:14px;">⚙️ 出题设置</h2>
        <div class="filter-row">
          <label>模式</label>
          <select class="pick" id="q-mode">
            <option value="smart">🎯 智能推荐（错题优先）</option>
            <option value="random">🔀 随机抽题</option>
            <option value="wrong">❌ 仅错题</option>
            <option value="new">🌱 只出没做过的题</option>
          </select>
          <label>题量</label>
          <select class="pick" id="q-count">
            <option>10</option><option selected>15</option><option>20</option>
            <option>30</option><option>50</option><option value="0">全部</option>
          </select>
        </div>
        <div class="filter-row">
          <label>难度</label>
          <div class="category-list" id="setup-levels" style="padding:0;"></div>
        </div>
        <div class="filter-row">
          <label>出处</label>
          <div class="category-list" id="setup-sources" style="padding:0;"></div>
        </div>
        <div style="margin:14px 0 8px; font-size:14px; font-weight:600;">考点分类（不选＝全部）</div>
        <div class="category-list" id="setup-categories"></div>
        <input type="text" id="setup-keyword" placeholder="🔍 关键词筛选，例如：冠词 / ten-minute / give / 介词" style="width:100%; margin-top:12px; padding:10px 14px; border:1.5px solid var(--border); border-radius:8px;" oninput="updatePreview()" />
        <div id="setup-preview"></div>
        <div style="display:flex; gap:10px; margin-top:16px;">
          <button class="btn btn-large" onclick="generateQuiz()">开始刷题</button>
          <button class="btn btn-secondary" onclick="resetSetup()">重置条件</button>
        </div>
      </div>
    </div>

    <div id="practice-quiz" style="display: none;">
      <div class="round-indicator" id="round-indicator">第 1 轮</div>
      <div id="questions-container"></div>
      <div style="display:flex; gap:10px; margin:18px 0 40px;">
        <button class="btn btn-large" onclick="submitQuiz()">提交答案</button>
        <button class="btn btn-secondary" onclick="printQuiz()">🖨 打印本轮</button>
        <button class="btn btn-secondary" onclick="startPractice()">换一批</button>
      </div>
    </div>

    <div id="practice-result" style="display: none;"></div>
  </section>

  <!-- ============ 知识点 ============ -->
  <section class="view" id="view-knowledge">
    <div class="card">
      <h2 style="font-size:17px; margin-bottom:6px;">📚 知识点速查</h2>
      <p style="font-size:12px; color:var(--text-light); margin-bottom:12px;">共 __KPCNT__ 个考点条目。点击分类跳转。</p>
      <div class="category-list" id="knowledge-categories"></div>
    </div>
    <div id="knowledge-content"></div>
  </section>

  <!-- ============ 错题本 ============ -->
  <section class="view" id="view-errors">
    <div class="card">
      <div id="error-stats" style="margin-bottom: 16px;"></div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <button class="btn btn-error" id="clear-errors-btn" onclick="clearErrors()">🗑️ 清空错题本</button>
        <button class="btn" id="practice-errors-btn" onclick="startWrongOnly()">❌ 重做全部错题</button>
      </div>
    </div>
    <div id="error-list"></div>
  </section>

  <!-- ============ 进度 ============ -->
  <section class="view" id="view-progress">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="num streak" id="prog-streak">0</div><div class="label">连续打卡（天）</div>
        <button class="reset-btn" id="reset-streak-btn" onclick="resetStreak()" style="display:none;" title="重置打卡天数">🔄</button>
      </div>
      <div class="stat-card"><div class="num" id="prog-answered">0</div><div class="label">累计答题</div></div>
      <div class="stat-card"><div class="num" id="prog-correct">0</div><div class="label">答对题数</div></div>
      <div class="stat-card"><div class="num" id="prog-mastered">0</div><div class="label">已攻克错题</div></div>
    </div>
    <div class="card"><h2 style="font-size:16px; margin-bottom:12px;">📈 各考点掌握情况</h2><div id="category-progress"></div></div>
    <div class="card"><h2 style="font-size:16px; margin-bottom:12px;">🎚️ 难度分布</h2><div id="level-progress"></div></div>
    <div class="card"><h2 style="font-size:16px; margin-bottom:12px;">📌 出处分布</h2><div id="source-progress"></div></div>
    <div class="card">
      <h2 style="font-size:16px; margin-bottom:12px;">📅 最近 7 天打卡</h2>
      <div id="streak-calendar" style="display:flex; gap:6px; flex-wrap:wrap;"></div>
    </div>
  </section>
</main>

<div id="print-header" class="print-only">
  六年级英语每日刷题 · __PRINT_TITLE__
  <div class="sub">姓名：__________　班级：__________　日期：__________　　共 __PRINT_N__ 题</div>
</div>

<script>
/* =====================================================================
   数据
===================================================================== */
const QUESTIONS = __QUESTIONS__;
const KNOWLEDGE_POINTS = __KNOWLEDGE__;
const CAT_COUNT = __CATLIST__;
const SRC_COUNT = __SRCLIST__;
const LVL_COUNT = __LVLLIST__;
const BUILD_DATE = "__BUILD_DATE__";

/* =====================================================================
   状态
===================================================================== */
const STORAGE_KEY = 'engPractice_v2';
let state = {
  streak: 0,
  lastPracticeDate: null,
  totalAnswered: 0,
  totalCorrect: 0,
  errorLog: {},   // id -> { times, mastered }
  seen: {},       // id -> 次数
  history: [],
  lastSaved: 0
};

let STORAGE_OK = true;

function loadState() {
  try {
    localStorage.setItem('__probe__', '1');
    localStorage.removeItem('__probe__');
  } catch (e) {
    STORAGE_OK = false;
    console.warn('localStorage 不可用，本次成绩不会被保存', e);
  }
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) state = Object.assign(state, JSON.parse(saved));
    // v1 数据迁移：保留旧版累计与错题
    const old = localStorage.getItem('engPractice_v1');
    if (old) {
      const o = JSON.parse(old);
      if (!state.totalAnswered && o.totalAnswered) {
        state.totalAnswered = o.totalAnswered;
        state.totalCorrect = o.totalCorrect || 0;
        state.streak = o.streak || 0;
        state.lastPracticeDate = o.lastPracticeDate || null;
      }
    }
  } catch (e) { console.error('Load state failed', e); }
}

function saveState() {
  try {
    const savedRaw = localStorage.getItem(STORAGE_KEY);
    if (savedRaw) {
      const existing = JSON.parse(savedRaw);
      if (existing.lastSaved && existing.lastSaved > (state.lastSaved || 0)) {
        state.totalAnswered = Math.max(state.totalAnswered, existing.totalAnswered || 0);
        state.totalCorrect = Math.max(state.totalCorrect, existing.totalCorrect || 0);
        const merged = Object.assign({}, existing.errorLog || {});
        for (const id in state.errorLog) {
          const l = state.errorLog[id], r = merged[id] || { times: 0, mastered: false };
          merged[id] = { times: Math.max(l.times || 0, r.times || 0), mastered: !!(l.mastered || r.mastered) };
        }
        state.errorLog = merged;
        state.lastSaved = existing.lastSaved;
        return;
      }
    }
    state.lastSaved = Date.now();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (e) { console.error('Save state failed', e); }
}

function mergeIncoming(incoming) {
  // 只接受更新的快照；计数取较大值，错题本取并集，避免旧标签页把新进度覆盖回去
  if (!incoming) return false;
  if (incoming.lastSaved && state.lastSaved && incoming.lastSaved < state.lastSaved) return false;
  state.streak = Math.max(state.streak || 0, incoming.streak || 0);
  state.totalAnswered = Math.max(state.totalAnswered || 0, incoming.totalAnswered || 0);
  state.totalCorrect = Math.max(state.totalCorrect || 0, incoming.totalCorrect || 0);
  if (incoming.lastPracticeDate) state.lastPracticeDate = incoming.lastPracticeDate;
  if (incoming.history && incoming.history.length > (state.history || []).length) state.history = incoming.history;
  const merged = Object.assign({}, state.errorLog || {});
  for (const id in (incoming.errorLog || {})) {
    const l = merged[id] || { times: 0, mastered: false };
    const r = incoming.errorLog[id];
    merged[id] = {
      times: Math.max(l.times || 0, r.times || 0),
      mastered: !!(l.mastered || r.mastered)
    };
  }
  state.errorLog = merged;
  const seen = Object.assign({}, state.seen || {});
  for (const id in (incoming.seen || {})) {
    seen[id] = Math.max(seen[id] || 0, incoming.seen[id]);
  }
  state.seen = seen;
  if (incoming.lastSaved) state.lastSaved = incoming.lastSaved;
  return true;
}

window.addEventListener('storage', (e) => {
  if (e.key === STORAGE_KEY && e.newValue) {
    try {
      if (!mergeIncoming(JSON.parse(e.newValue))) return;
      const v = document.querySelector('.view.active');
      if (v) {
        const id = v.id.replace('view-', '');
        if (id === 'home') renderHome();
        if (id === 'errors') renderErrors();
        if (id === 'progress') renderProgress();
      }
      showSyncNotice();
    } catch (err) { console.error('Sync failed', err); }
  }
});

function showSyncNotice() {
  let n = document.getElementById('sync-notice');
  if (!n) {
    n = document.createElement('div');
    n.id = 'sync-notice';
    n.style.cssText = 'position:fixed;top:80px;left:50%;transform:translateX(-50%);background:#5BC85B;color:#fff;padding:10px 20px;border-radius:20px;font-size:13px;z-index:9999;box-shadow:0 4px 12px rgba(0,0,0,.15);opacity:0;transition:opacity .3s;';
    document.body.appendChild(n);
  }
  n.textContent = '🔄 数据已从其他窗口同步';
  n.style.opacity = '1';
  setTimeout(() => { n.style.opacity = '0'; }, 2000);
}

/* =====================================================================
   导航
===================================================================== */
function showView(name) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + name).classList.add('active');
  document.querySelectorAll('nav button').forEach(b => b.classList.toggle('active', b.dataset.view === name));
  window.scrollTo({ top: 0, behavior: 'smooth' });
  if (name === 'home') renderHome();
  if (name === 'errors') renderErrors();
  if (name === 'progress') renderProgress();
  if (name === 'knowledge') renderKnowledge();
  if (name === 'practice') renderSetupPanel();
}

document.querySelectorAll('nav button').forEach(b => {
  b.addEventListener('click', () => showView(b.dataset.view));
});

/* =====================================================================
   首页
===================================================================== */
function renderHome() {
  document.getElementById('storage-warn').style.display = STORAGE_OK ? 'none' : 'block';
  document.getElementById('home-streak').textContent = state.streak;
  document.getElementById('home-answered').textContent = state.totalAnswered;
  document.getElementById('home-accuracy').textContent = state.totalAnswered > 0
    ? Math.round(state.totalCorrect / state.totalAnswered * 100) + '%' : '0%';
  document.getElementById('home-mastered').textContent = Object.values(state.errorLog).filter(e => e.mastered).length;
  const pend = Object.entries(state.errorLog).filter(([, v]) => !v.mastered).length;
  document.getElementById('qc-wrong').textContent = pend > 0 ? ('待掌握 ' + pend + ' 题') : '错题本为空';
  renderCategories(document.getElementById('home-categories'), false);
}

function renderCategories(container, multiSelect) {
  const cats = [...new Set(QUESTIONS.map(q => q.category))];
  container.innerHTML = cats.map(c =>
    `<span class="category-chip" data-cat="${c}">${c}<span class="chip-count">${CAT_COUNT[c] || 0}</span></span>`).join('');
  container.querySelectorAll('.category-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      if (multiSelect) {
        chip.classList.toggle('active');
        updatePreview();
      } else {
        pendingCat = chip.dataset.cat;
        showView('practice');
      }
    });
  });
}

function searchByKeyword() {
  document.getElementById('setup-keyword').value = document.getElementById('keyword-input').value.trim();
  showView('practice');
  renderSetupPanel();
  document.getElementById('setup-keyword').value = document.getElementById('keyword-input').value.trim();
  updatePreview();
}

/* =====================================================================
   刷题
===================================================================== */
let currentQuestions = [];
let currentAnswers = {};
let currentRound = 1;
let currentWrongIds = [];
let currentMeta = { title: '综合练习' };

let pendingCat = null;

function startPractice() {
  showView('practice');
  renderSetupPanel();
  document.getElementById('practice-quiz').style.display = 'none';
  document.getElementById('practice-result').style.display = 'none';
}

function renderSetupPanel() {
  document.getElementById('practice-setup').style.display = 'block';
  renderCategories(document.getElementById('setup-categories'), true);
  renderPickChips('setup-levels', LVL_COUNT, 'lv');
  renderPickChips('setup-sources', SRC_COUNT, 'src');
  if (pendingCat) {
    document.querySelectorAll('#setup-categories .category-chip').forEach(chip => {
      if (chip.dataset.cat === pendingCat) chip.classList.add('active');
    });
    pendingCat = null;
  }
  updatePreview();
}

function renderPickChips(id, counts, kind) {
  const box = document.getElementById(id);
  box.innerHTML = Object.entries(counts).map(([k, v]) =>
    `<span class="category-chip" data-kind="${kind}" data-val="${k}">${k}<span class="chip-count">${v}</span></span>`).join('');
  box.querySelectorAll('.category-chip').forEach(chip => {
    chip.addEventListener('click', () => { chip.classList.toggle('active'); updatePreview(); });
  });
}

function resetSetup() {
  document.getElementById('q-mode').value = 'smart';
  document.getElementById('q-count').value = '15';
  document.getElementById('setup-keyword').value = '';
  document.querySelectorAll('#setup-categories .category-chip.active').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('#setup-levels .category-chip.active').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('#setup-sources .category-chip.active').forEach(c => c.classList.remove('active'));
  updatePreview();
}

function pickedChips(containerId) {
  return [...document.getElementById(containerId).querySelectorAll('.category-chip.active')].map(c => c.dataset.val || c.dataset.cat);
}

function buildPool() {
  const cats = pickedChips('setup-categories');
  const levels = pickedChips('setup-levels');
  const sources = pickedChips('setup-sources');
  const kw = document.getElementById('setup-keyword').value.trim().toLowerCase();
  return QUESTIONS.filter(q => {
    if (cats.length && !cats.includes(q.category)) return false;
    if (levels.length && !levels.includes(q.level)) return false;
    if (sources.length && !sources.includes(q.source)) return false;
    if (kw) {
      const hay = (q.question + ' ' + q.explanation + ' ' + q.point + ' ' + q.category + ' ' + q.tags.join(' ')).toLowerCase();
      if (!hay.includes(kw)) return false;
    }
    return true;
  });
}

function updatePreview() {
  const pool = buildPool();
  const el = document.getElementById('setup-preview');
  if (!el) return;
  const errs = Object.entries(state.errorLog).filter(([id, v]) => !v.mastered && pool.some(q => String(q.id) === id));
  el.innerHTML = `符合条件 <strong>${pool.length}</strong> 题　·　其中待攻克错题 <strong style="color:var(--error)">${errs.length}</strong> 题`;
}

function generateQuiz() {
  const mode = document.getElementById('q-mode').value;
  let count = parseInt(document.getElementById('q-count').value);
  let pool = buildPool();
  if (!pool.length) { alert('没有符合条件的题目，请放宽筛选条件。'); return; }
  if (count === 0 || count > pool.length) count = pool.length;

  let chosen = [];
  if (mode === 'wrong') {
    const ids = Object.entries(state.errorLog).filter(([, v]) => !v.mastered).map(([id]) => Number(id));
    chosen = pool.filter(q => ids.includes(q.id));
    if (!chosen.length) { alert('当前条件下没有待掌握的错题。'); return; }
    chosen = shuffle(chosen).slice(0, count);
  } else if (mode === 'new') {
    chosen = shuffle(pool.filter(q => !state.seen[q.id])).slice(0, count);
    if (chosen.length < count) chosen = chosen.concat(shuffle(pool.filter(q => state.seen[q.id])).slice(0, count - chosen.length));
  } else if (mode === 'random') {
    chosen = shuffle(pool).slice(0, count);
  } else {
    // 智能：待掌握错题优先，其次是没做过的，最后是已做过的
    const errIds = Object.entries(state.errorLog).filter(([, v]) => !v.mastered).map(([id]) => Number(id));
    const errs = shuffle(pool.filter(q => errIds.includes(q.id)));
    const fresh = shuffle(pool.filter(q => !state.seen[q.id] && !errIds.includes(q.id)));
    const old = shuffle(pool.filter(q => state.seen[q.id] && !errIds.includes(q.id)));
    chosen = errs.concat(fresh).concat(old).slice(0, count);
  }
  currentQuestions = chosen;
  currentAnswers = {};
  currentRound = 1;
  currentWrongIds = [];
  const modeTitle = { smart: '智能推荐', random: '随机抽题', wrong: '错题重练', new: '新题练习' }[mode] || '综合练习';
  const scope = pickedChips('setup-categories');
  currentMeta = { title: modeTitle + (scope.length === 1 ? ' · ' + scope[0] : '') };
  document.getElementById('practice-setup').style.display = 'none';
  document.getElementById('practice-result').style.display = 'none';
  document.getElementById('practice-quiz').style.display = 'block';
  renderQuiz();
  document.getElementById('practice-quiz').scrollIntoView({ behavior: 'smooth' });
}

function startSmart(n) {
  showView('practice');
  document.getElementById('practice-setup').style.display = 'none';
  document.getElementById('practice-quiz').style.display = 'none';
  document.getElementById('practice-result').style.display = 'none';
  document.getElementById('q-mode').value = 'smart';
  document.getElementById('q-count').value = String(n);
  document.getElementById('setup-keyword').value = '';
  document.querySelectorAll('#setup-categories .category-chip.active').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('#setup-levels .category-chip.active').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('#setup-sources .category-chip.active').forEach(c => c.classList.remove('active'));
  currentMeta = { title: '每日 ' + n + ' 题 · 智能推荐' };
  generateQuiz();
}

function startRandom(n) {
  showView('practice');
  document.getElementById('q-mode').value = 'random';
  document.getElementById('q-count').value = String(n);
  currentMeta = { title: '随机 ' + n + ' 题' };
  generateQuiz();
}

function startWrongOnly() {
  showView('practice');
  document.getElementById('q-mode').value = 'wrong';
  document.getElementById('q-count').value = '0';
  document.getElementById('setup-keyword').value = '';
  document.querySelectorAll('#setup-categories .category-chip.active').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('#setup-levels .category-chip.active').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('#setup-sources .category-chip.active').forEach(c => c.classList.remove('active'));
  currentMeta = { title: '错题重练' };
  generateQuiz();
}

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function renderQuiz() {
  document.getElementById('round-indicator').textContent =
    `${currentMeta.title}　·　第 ${currentRound} 轮 · ${currentQuestions.length} 题`;
  const container = document.getElementById('questions-container');
  container.innerHTML = currentQuestions.map((q, idx) => `
    <div class="question-card" data-qid="${q.id}">
      <div class="q-header">
        <span class="q-num">${idx + 1}</span>
        <div class="q-meta">
          <span class="badge lv-${q.level}">${q.level}</span>
          <span class="badge src">${q.source}</span>
          <span class="q-tag" style="display:none;">${q.category} · ${q.point}</span>
        </div>
      </div>
      <div class="q-text">${escapeHtml(q.question)}</div>
      <div class="q-options">
        ${q.options.map((v, i) => `
          <div class="q-option" data-key="${'ABCD'[i]}" onclick="selectOption(${idx}, '${'ABCD'[i]}', this)">
            <strong>${'ABCD'[i]}.</strong> ${escapeHtml(v)}
          </div>`).join('')}
      </div>
      <div class="q-explanation" style="display:none;"></div>
    </div>`).join('');
}

function selectOption(qIdx, key, el) {
  const card = el.closest('.question-card');
  card.querySelectorAll('.q-option').forEach(o => o.classList.remove('selected'));
  el.classList.add('selected');
  currentAnswers[qIdx] = key;
}

function submitQuiz() {
  const unanswered = [];
  currentQuestions.forEach((_, idx) => { if (!currentAnswers[idx]) unanswered.push(idx + 1); });
  if (unanswered.length > 0) {
    if (!confirm(`还有 ${unanswered.length} 题没答（${unanswered.join(', ')}），确定提交吗？`)) return;
  }
  updateStreak();
  let correctCount = 0;
  const wrongQuestions = [];

  currentQuestions.forEach((q, idx) => {
    const userAns = currentAnswers[idx];
    const card = document.querySelector(`.question-card[data-qid="${q.id}"]`);
    const options = card.querySelectorAll('.q-option');
    const isCorrect = userAns === q.answer;
    if (isCorrect) {
      correctCount++;
      card.classList.add('correct');
      card.querySelector('.q-num').classList.add('correct');
    } else {
      card.classList.add('wrong');
      card.querySelector('.q-num').classList.add('wrong');
      wrongQuestions.push(q);
    }
    options.forEach(o => {
      const k = o.dataset.key;
      if (k === q.answer) o.classList.add('correct');
      else if (k === userAns && !isCorrect) o.classList.add('wrong');
    });
    const exp = card.querySelector('.q-explanation');
    exp.innerHTML = `<strong>语法点：</strong>${q.category} · ${q.point}　<span class="badge src">${q.source}</span><br>`
      + `<strong>解析：</strong>${q.explanation}<br><strong>正确答案：</strong>${q.answer}. ${escapeHtml(q.options['ABCD'.indexOf(q.answer)])}`;
    exp.style.display = 'block';
    const tag = card.querySelector('.q-tag');
    if (tag) tag.style.display = 'inline-block';

    state.totalAnswered++;
    state.seen[q.id] = (state.seen[q.id] || 0) + 1;
    if (isCorrect) state.totalCorrect++;
    if (!isCorrect) {
      if (!state.errorLog[q.id]) state.errorLog[q.id] = { times: 0, mastered: false };
      state.errorLog[q.id].times++;
      state.errorLog[q.id].mastered = false;
    } else if (state.errorLog[q.id]) {
      state.errorLog[q.id].mastered = true;
    }
  });

  saveState();
  const resultDiv = document.getElementById('practice-result');
  const total = currentQuestions.length;
  currentWrongIds = wrongQuestions.map(q => q.id);
  state.history.push({ date: new Date().toDateString(), score: correctCount, total });
  if (state.history.length > 400) state.history = state.history.slice(-400);
  saveState();

  const bannerClass = correctCount === total ? 'success' : 'partial';
  const bannerText = correctCount === total
    ? '🎉 完美通关！全部答对！'
    : (correctCount >= total * 0.7 ? '👍 不错！还有一些需要巩固。' : '💪 别灰心，错题是进步的阶梯！');

  resultDiv.innerHTML = `
    <div class="result-banner ${bannerClass}">
      <div class="big-num">${correctCount}/${total}</div>
      <div class="label">${bannerText}</div>
    </div>
    <div class="actions">
      ${currentWrongIds.length > 0
        ? `<button class="btn btn-error btn-large" onclick="regenerateWrong()">🔄 重做错题（${currentWrongIds.length} 题）</button>`
        : `<button class="btn btn-success btn-large" onclick="finishPractice()">🎯 完成</button>`}
      <button class="btn btn-secondary" onclick="startSmart(10)">🎯 每日 10 题</button>
      <button class="btn btn-secondary" onclick="showView('home')">🏠 返回首页</button>
    </div>`;
  resultDiv.style.display = 'block';
  resultDiv.scrollIntoView({ behavior: 'smooth' });
}

function regenerateWrong() {
  if (!currentWrongIds.length) return finishPractice();
  const wrongSet = new Set(currentWrongIds);
  const wrongPoints = new Set();
  currentQuestions.forEach(q => { if (wrongSet.has(q.id)) wrongPoints.add(q.category); });
  let pool = QUESTIONS.filter(q => wrongPoints.has(q.category) && !wrongSet.has(q.id));
  if (pool.length < currentWrongIds.length) pool = pool.concat(QUESTIONS.filter(q => wrongSet.has(q.id)));
  currentQuestions = shuffle(pool).slice(0, currentWrongIds.length);
  currentAnswers = {};
  currentRound++;
  document.getElementById('practice-result').style.display = 'none';
  renderQuiz();
  document.getElementById('practice-quiz').scrollIntoView({ behavior: 'smooth' });
}

function finishPractice() {
  showView('home');
}

/* =====================================================================
   打印
===================================================================== */
function printQuiz() {
  const ph = document.getElementById('print-header');
  ph.innerHTML = `六年级英语每日刷题 · ${currentMeta.title}`
    + `<div class="sub">姓名：__________　班级：__________　日期：__________　　共 ${currentQuestions.length} 题</div>`;
  ph.querySelector('.sub').className = 'sub';
  const cont = document.getElementById('questions-container');
  const orig = cont.innerHTML;
  // 打印版：去掉已选样式与解析
  const paper = cont.cloneNode(true);
  paper.querySelectorAll('.q-explanation').forEach(e => e.style.display = 'none');
  paper.querySelectorAll('.q-option.selected, .q-option.correct, .q-option.wrong').forEach(e => e.classList.remove('selected', 'correct', 'wrong'));
  paper.querySelectorAll('.q-tag').forEach(e => e.style.display = 'none');
  cont.parentNode.insertBefore(paper, cont);
  cont.style.display = 'none';
  const restore = () => {
    paper.remove();
    cont.style.display = '';
    window.removeEventListener('afterprint', restore);
  };
  window.addEventListener('afterprint', restore);
  window.print();
  setTimeout(restore, 1500);
}

/* =====================================================================
   知识点
===================================================================== */
function renderKnowledge() {
  const cats = [...new Set(KNOWLEDGE_POINTS.map(k => k.category))];
  document.getElementById('knowledge-categories').innerHTML = cats.map(c => {
    const n = (KNOWLEDGE_POINTS.find(k => k.category === c).points || []).length;
    return `<span class="category-chip" data-cat="${c}">${c}<span class="chip-count">${n}</span></span>`;
  }).join('');
  document.querySelectorAll('#knowledge-categories .category-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const t = document.getElementById('kp-' + chip.dataset.cat.replace(/[^a-zA-Z]/g, ''));
      if (t) t.scrollIntoView({ behavior: 'smooth' });
    });
  });
  document.getElementById('knowledge-content').innerHTML = KNOWLEDGE_POINTS.map(kp => `
    <div class="card grammar-section" id="kp-${kp.category.replace(/[^a-zA-Z]/g, '')}">
      <div class="kp-head">
        <h2 style="font-size:17px;">${kp.icon} ${kp.category}</h2>
        <span class="badge lv-${kp.level}">${kp.level}</span>
      </div>
      ${kp.points.map(p => `
        <div class="point" style="font-weight:600; margin-top:14px;">▸ ${p.name}</div>
        <div style="margin:4px 0 6px; color:var(--text-light); font-size:14px; line-height:1.7;">${p.rule}</div>
        ${(p.examples || []).map(e => `<div class="example">${escapeHtml(e)}</div>`).join('')}
        ${p.warn ? `<div class="kp-warn">⚠️ ${escapeHtml(p.warn)}</div>` : ''}
        ${p.tip ? `<div class="kp-tip">💡 ${escapeHtml(p.tip)}</div>` : ''}
      `).join('')}
    </div>`).join('');
}

/* =====================================================================
   错题本
===================================================================== */
function renderErrors() {
  const entries = Object.entries(state.errorLog).map(([id, v]) => ({
    q: QUESTIONS.find(qq => qq.id == id), ...v
  })).filter(e => e.q);
  const total = entries.length;
  const mastered = entries.filter(e => e.mastered).length;
  const pending = total - mastered;

  document.getElementById('error-stats').innerHTML = `
    <div style="display:flex; gap:16px; flex-wrap:wrap; margin-bottom:10px;">
      <div><strong style="color:var(--error); font-size:20px;">${pending}</strong> 待掌握</div>
      <div><strong style="color:var(--success); font-size:20px;">${mastered}</strong> 已掌握</div>
      <div><strong style="color:var(--primary); font-size:20px;">${total}</strong> 总错题数</div>
    </div>
    <div class="progress-bar"><div class="progress-bar-fill" style="width:${total > 0 ? (mastered / total * 100) : 0}%"></div></div>`;
  document.getElementById('clear-errors-btn').style.display = total > 0 ? 'inline-block' : 'none';
  document.getElementById('practice-errors-btn').style.display = pending > 0 ? 'inline-block' : 'none';

  if (total === 0) {
    document.getElementById('error-list').innerHTML = `
      <div class="card"><div class="empty-state"><div class="emoji">🎉</div><div>错题本是空的！继续保持！</div></div></div>`;
    return;
  }
  const pendingList = entries.filter(e => !e.mastered).sort((a, b) => b.times - a.times);
  const masteredList = entries.filter(e => e.mastered);
  document.getElementById('error-list').innerHTML = `
    ${pendingList.length ? '<h3 style="margin:18px 0 10px; color:var(--error);">📌 待掌握的错题</h3>' : ''}
    ${pendingList.map(renderErrorItem).join('')}
    ${masteredList.length ? '<h3 style="margin:24px 0 10px; color:var(--success);">✅ 已掌握</h3>' : ''}
    ${masteredList.map(renderErrorItem).join('')}`;
}

function renderErrorItem(e) {
  return `
    <div class="card error-list-item ${e.mastered ? 'mastered' : ''}">
      <div style="font-weight:600; margin-bottom:6px;">${e.mastered ? '✅' : '❌'} ${escapeHtml(e.q.question)}</div>
      <div class="meta-row">${e.q.category} · ${e.q.point} · ${e.q.level} · ${e.q.source} · 错了 ${e.times} 次 · 正确答案: ${e.q.answer}. ${escapeHtml(e.q.options['ABCD'.indexOf(e.q.answer)])}</div>
      <div style="margin-top:6px; font-size:13px; color:var(--text-light);">${e.q.explanation}</div>
    </div>`;
}

function clearErrors() {
  if (confirm('确定清空所有错题记录吗？此操作不可恢复。')) {
    state.errorLog = {};
    saveState();
    renderErrors();
  }
}

/* =====================================================================
   进度
===================================================================== */
function renderProgress() {
  document.getElementById('prog-streak').textContent = state.streak;
  document.getElementById('prog-answered').textContent = state.totalAnswered;
  document.getElementById('prog-correct').textContent = state.totalCorrect;
  document.getElementById('prog-mastered').textContent = Object.values(state.errorLog).filter(e => e.mastered).length;
  document.getElementById('reset-streak-btn').style.display = state.streak > 0 ? 'inline-block' : 'none';

  const catStats = {};
  QUESTIONS.forEach(q => {
    if (!catStats[q.category]) catStats[q.category] = { total: 0, errors: 0 };
    catStats[q.category].total++;
    if (state.errorLog[q.id] && !state.errorLog[q.id].mastered) catStats[q.category].errors++;
  });
  document.getElementById('category-progress').innerHTML = Object.entries(catStats)
    .sort((a, b) => (b[1].errors - b[1].total / 100) - (a[1].errors - a[1].total / 100))
    .map(([cat, s]) => {
      const pct = s.total > 0 ? ((s.total - s.errors) / s.total * 100) : 100;
      return `<div style="margin-bottom:12px;">
        <div style="display:flex; justify-content:space-between; font-size:14px;">
          <span>${cat}</span><span style="color:var(--text-light);">${s.total - s.errors}/${s.total} 掌握</span></div>
        <div class="progress-bar"><div class="progress-bar-fill" style="width:${pct}%"></div></div></div>`;
    }).join('');

  const groupStat = (key) => {
    const m = {};
    QUESTIONS.forEach(q => {
      const k = q[key];
      if (!m[k]) m[k] = { total: 0, errors: 0 };
      m[k].total++;
      if (state.errorLog[q.id] && !state.errorLog[q.id].mastered) m[k].errors++;
    });
    return Object.entries(m).map(([k, s]) => {
      const pct = s.total > 0 ? ((s.total - s.errors) / s.total * 100) : 100;
      return `<div style="margin-bottom:12px;">
        <div style="display:flex; justify-content:space-between; font-size:14px;">
          <span>${k}</span><span style="color:var(--text-light);">${s.total - s.errors}/${s.total} 掌握</span></div>
        <div class="progress-bar"><div class="progress-bar-fill" style="width:${pct}%"></div></div></div>`;
    }).join('');
  };
  document.getElementById('level-progress').innerHTML = groupStat('level');
  document.getElementById('source-progress').innerHTML = groupStat('source');

  const cal = document.getElementById('streak-calendar');
  const today = new Date();
  let html = '';
  for (let i = 6; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    const isToday = i === 0;
    const dateStr = d.toDateString();
    const practiced = state.lastPracticeDate && new Date(state.lastPracticeDate).toDateString() === dateStr;
    html += `<div style="text-align:center;">
      <div style="font-size:11px; color:var(--text-light);">${['日','一','二','三','四','五','六'][d.getDay()]}</div>
      <div style="width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;
        background:${practiced ? 'var(--success)' : 'var(--border)'};color:${practiced ? 'white' : 'var(--text-light)'};
        font-weight:${isToday ? '700' : '500'};border:${isToday ? '2px solid var(--primary)' : 'none'};">${d.getDate()}</div></div>`;
  }
  cal.innerHTML = html;
}

/* =====================================================================
   工具
===================================================================== */
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

function updateStreak() {
  const today = new Date().toDateString();
  if (!state.lastPracticeDate) {
    state.streak = 1;
  } else {
    const last = new Date(state.lastPracticeDate);
    const diff = Math.floor((new Date(today) - last) / (1000 * 60 * 60 * 24));
    if (diff === 1) state.streak++;
    else if (diff > 1) state.streak = 1;
  }
  state.lastPracticeDate = new Date().toISOString();
}

function resetStreak() {
  if (!confirm('确定要重置连续打卡天数吗？此操作不会清除答题记录和错题本。')) return;
  state.streak = 0;
  state.lastPracticeDate = null;
  saveState();
  renderProgress();
  renderHome();
  alert('✅ 连续打卡天数已重置为 0。');
}

/* 启动 */
loadState();
renderHome();

window.startPractice = startPractice;
window.generateQuiz = generateQuiz;
window.submitQuiz = submitQuiz;
window.selectOption = selectOption;
window.regenerateWrong = regenerateWrong;
window.finishPractice = finishPractice;
window.searchByKeyword = searchByKeyword;
window.showView = showView;
window.clearErrors = clearErrors;
window.resetStreak = resetStreak;
window.startSmart = startSmart;
window.startRandom = startRandom;
window.startWrongOnly = startWrongOnly;
window.resetSetup = resetSetup;
window.printQuiz = printQuiz;
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
