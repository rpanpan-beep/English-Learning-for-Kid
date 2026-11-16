# -*- coding: utf-8 -*-
# 语音（元音 / 辅音与重音）/ 词形转换 / 名词与数词 —— 每日刷题 v2
# 分类条数：语音·元音 10 条，语音·辅音与重音 8 条，词形转换 20 条，名词与数词 10 条，共 48 条。

Q = [
    # ==================== 语音·元音（10） ====================
    ("语音·元音", "字母 a 与 ai/ay 辨音", "🟢", "6A教材",
     "Choose the word with a different pronunciation.",
     ["rain", "day", "hat", "wait"], "C",
     "rain /reɪn/、day /deɪ/、wait /weɪt/ 中的 ai、ay 都读 /eɪ/；只有 hat /hæt/ 中的 a 读 /æ/，"
     "与其他三个不同，故选 C。（science /ˈsaɪəns/ 中的 ai 也是 /eɪ/，可一起记）",
     ["元音辨音", "字母a", "ai/ay"]),

    ("语音·元音", "字母 e 与 ee/ea 辨音", "🟡", "6A教材",
     "Choose the word with a different pronunciation.",
     ["need", "eat", "read", "head"], "D",
     "need /niːd/、eat /iːt/、read /riːd/ 中的 ee、ea 都读 /iː/；head /hed/ 中的 ea 读 /e/，"
     "故选 D。口诀：<strong>同一个字母组合，音不同就要停下来</strong>。",
     ["元音辨音", "ee/ea", "字母e"]),

    ("语音·元音", "字母 o 的两种读音", "🟢", "兰生9月月考",
     "Choose the word with a different pronunciation.",
     ["photo", "shop", "clock", "hot"], "A",
     "shop /ʃɒp/、clock /klɒk/、hot /hɒt/ 中的 o 都读短音 /ɒ/；photo /ˈfəʊtəʊ/ 中的 o 读 /əʊ/，故选 A。",
     ["元音辨音", "字母o", "/ɒ/与/əʊ/"]),

    ("语音·元音", "字母 u 与 ou 辨音", "🟡", "6A教材",
     "Choose the word with a different pronunciation.",
     ["bus", "house", "cup", "sun"], "B",
     "bus /bʌs/、cup /kʌp/、sun /sʌn/ 中的 u 都读 /ʌ/；house /haʊs/ 中的 ou 读 /aʊ/，故选 B。"
     "（music /ˈmjuːzɪk/ 中 u 读 /juː/，也常考）",
     ["元音辨音", "字母u", "ou"]),

    ("语音·元音", "oo 与 ow 读音辨析", "🟡", "兰生9月月考",
     "Choose the word with a different pronunciation.",
     ["food", "moon", "zoo", "know"], "D",
     "food /fuːd/、moon /muːn/、zoo /zuː/ 中的 oo 都读 /uː/；know /nəʊ/ 中的 ow 读 /əʊ/，故选 D。"
     "short 的 oo 才读 /ʊ/，如 book /bʊk/。",
     ["元音辨音", "oo", "ow"]),

    ("语音·元音", "ar/er/ir/ur 辨音", "🔴", "6A教材",
     "Choose the word with a different pronunciation.",
     ["hard", "third", "bird", "girl"], "A",
     "third /θɜːd/、bird /bɜːd/、girl /ɡɜːl/ 中的 er、ir、ur 都读 /ɜː/；hard /hɑːd/ 中的 ar 读 /ɑː/，故选 A。"
     "注意 third 中的 th 读清辅音 /θ/。",
     ["元音辨音", "r音节", "ar/er/ir/ur"]),

    ("语音·元音", "看音标写单词 ow", "🟡", "练习册错题",
     "Now, I will ___ /ʃəʊ/ you around our school.",
     ["shoe", "show", "shore", "short"], "B",
     "/ʃəʊ/ = sh 加 ow 的读音，show /ʃəʊ/ 拼写为 s-h-o-w，且放进句子“带你参观我们学校”最通顺；"
     "shoe /ʃuː/、shore /ʃɔː/、short /ʃɔːt/ 的元音都不是 /əʊ/，故选 B。",
     ["音标写单词", "ow", "拼写"]),

    ("语音·元音", "看音标写单词 ai", "🟢", "兰生9月月考",
     "We should enjoy ___ /laɪf/ at school, not only study.",
     ["live", "lief", "lif", "life"], "D",
     "life /laɪf/ 中 i 读 /aɪ/（与 science /ˈsaɪəns/ 相同），life 也是“生活”的意思，符合 enjoy ___ at school；"
     "live /lɪv/ 读 /ɪ/，lief、lif 拼不成词，故选 D。",
     ["音标写单词", "ai", "life"]),

    ("语音·元音", "看音标写单词 -ed", "🟡", "6A教材",
     "He ___ /ˈwɒntɪd/ to join the Science Club last term.",
     ["wantid", "want", "wanted", "wantedd"], "C",
     "过去式 wanted /ˈwɒntɪd/ 中 -ed 读 /ɪd/，前面的 o 弱化为 /ɒ/，所以要写成 wanted；"
     "want 是动词原形，wantid、wantedd 是拼写错误，故选 C。",
     ["音标写单词", "-ed", "元音"]),

    ("语音·元音", "看音标写单词 u", "🟢", "6AU1知识单",
     "He has joined the Science ___ /ˈklʌb/ for two years.",
     ["club", "clubs", "cloub", "clubb"], "A",
     "club /ˈklʌb/ 中 u 读 /ʌ/；has joined ... for two years 讲的是加入一个俱乐部，用单数 club，"
     "clubs 表示复数不合句意，cloub、clubb 拼写错误，故选 A。",
     ["音标写单词", "字母u", "6AU1"]),

    # ==================== 语音·辅音与重音（8） ====================
    ("语音·辅音与重音", "看音标写单词 v 音", "🟡", "练习册错题",
     "Your school bag is so ___ /hevi/, Peter.",
     ["heive", "hary", "heavy", "hevy"], "C",
     "heavy /ˈhevi/ 是 h-e-a-v-y，中间是字母 v 发 /v/（上齿咬下唇，不是 /w/）；heive 把 a 写成了 i "
     "又多一个 e，hary 中的 a 不读 /e/，hevy 少了一个 e，三者都拼不出 /hevi/，故选 C。",
     ["音标写单词", "v音", "拼写"]),

    ("语音·辅音与重音", "看音标写单词 w 与 sh", "🟡", "6A教材",
     "We must ___ /wɒʃ/ our hands before dinner.",
     ["watch", "wosh", "wash", "woshing"], "C",
     "/wɒʃ/ 由 w 和 sh 组成：w 读 /w/、sh 读 /ʃ/，wash /wɒʃ/ 符合“饭前要洗手”；"
     "watch /wɒtʃ/ 的 ch 读 /tʃ/，wosh、woshing 拼写错误，故选 C。",
     ["音标写单词", "w音", "sh音"]),

    ("语音·辅音与重音", "s 与 z 清浊辨音", "🟢", "6A教材",
     "Choose the word with a different pronunciation.",
     ["is", "cats", "has", "his"], "B",
     "is /ɪz/、has /hæz/、his /hɪz/ 词尾的 s 都读浊辅音 /z/；cats /kæts/ 中的 s 读清辅音 /s/，故选 B。",
     ["辅音辨音", "s", "z"]),

    ("语音·辅音与重音", "th 清浊辅音辨析", "🟡", "6A教材",
     "Choose the word with a different pronunciation.",
     ["mother", "brother", "weather", "three"], "D",
     "mother /ˈmʌðə/、brother /ˈbrʌðə/、weather /ˈweðə/ 中的 th 读浊辅音 /ð/（声带要振动）；"
     "three /θriː/ 中的 th 读清辅音 /θ/，故选 D。",
     ["辅音辨音", "th", "清浊"]),

    ("语音·辅音与重音", "-ed 读 /t/ 的辨音", "🟡", "6A教材",
     "Choose the word with a different pronunciation.",
     ["wanted", "walked", "talked", "finished"], "A",
     "walked /wɔːkt/、talked /tɔːkt/、finished /ˈfɪnɪʃt/ 词尾都读清辅音 /t/；其中 k 读 /k/（字母 c 和 k "
     "都读 /k/，如 class /klɑːs/、science /ˈsaɪəns/），talked 中 ch 读 /tʃ/，finished 中 f 读 /f/；"
     "wanted /ˈwɒntɪd/ 读 /ɪd/，故选 A。",
     ["辅音辨音", "-ed", "清辅音"]),

    ("语音·辅音与重音", "v 与 w 辨音", "🟡", "6A教材",
     "Choose the word with a different pronunciation.",
     ["vet", "wet", "very", "want"], "D",
     "vet /vet/、wet /wet/、very /ˈveri/ 中都是字母 v 发 /v/（上齿咬下唇）；want /wɒnt/ 用 w 发 /w/（圆唇），"
     "故选 D。",
     ["辅音辨音", "v", "w"]),

    ("语音·辅音与重音", "重音在第二个音节", "🟡", "6A考纲",
     "Choose the word with the stress on the second syllable.",
     ["ˈteacher", "aˈbout", "ˈhandwriting", "ˈplayground"], "B",
     "只有 aˈbout /əˈbaʊt/ 的重音落在第二个音节；teacher /ˈtiːtʃə/、handwriting /ˈhændrɪtɪŋ/、"
     "playground /ˈpleɪɡraʊnd/ 都重读第一音节。teacher 中 ch 读 /tʃ/，handwriting 中 h 读 /h/，"
     "playground 中 g 读 /ɡ/，别读错，故选 B。",
     ["重音", "音节", "6AU1"]),

    ("语音·辅音与重音", "重音在第一个音节", "🔴", "6A考纲",
     "Choose the word with the stress on the first syllable.",
     ["ˈjunior", "acˈtivity", "inforˈmation", "deˈcision"], "A",
     "junior /ˈdʒuːniə(r)/ 重读第一音节，其中的 j 音 /dʒ/ 与 sh、ch 不同；activity 重音在 -tiv-，"
     "information 重音在 -ma-，decision /dɪˈsɪʒn/ 重音在第二音节，故选 A。",
     ["重音", "音节", "多音节词"]),

    # ==================== 词形转换（20） ====================
    ("词形转换", "动词变形容词 useful", "🟡", "练习册错题",
     "Thanks for telling me some ___ (use) information.",
     ["use", "useful", "useless", "user"], "B",
     "useful /ˈjuːsfl/ 是形容词“有用的”，用来修饰名词 information；use 是动词原形，"
     "useless 意思相反，user 是名词“使用者”，故选 B。",
     ["词形转换", "动词转形容词", "useful"]),

    ("词形转换", "动词变动名词 reading", "🟢", "练习册错题",
     "Do you love ___ (read) books?",
     ["read", "reads", "reader", "reading"], "D",
     "love 后要接<strong>动名词</strong> doing，所以填 read 的动名词 reading；read 是原形，"
     "reads 是第三人称单数，reader 是“读者”，故选 D。",
     ["词形转换", "动名词", "love doing"]),

    ("词形转换", "story 变 stories", "🟢", "练习册错题",
     "There are two ___ (story) in the book.",
     ["storys", "story", "stories", "storied"], "C",
     "story 是“辅音字母 + y”结尾，复数要<strong>去 y 加 ies</strong>，即 stories；storys 是最常见的错写，"
     "storied 是别的词，故选 C。",
     ["词形转换", "名词复数", "辅音+y"]),

    ("词形转换", "be glad to do", "🟡", "练习册错题",
     "I'm very glad ___ (meet) you here, boys and girls.",
     ["meet", "to meet", "meeting", "met"], "B",
     "<strong>be glad to do sth.</strong> 是固定搭配“很高兴做某事”，glad 后面要接动词不定式 to meet；"
     "meet 是原形，meeting 是动名词，met 是过去式，故选 B。",
     ["词形转换", "不定式", "固定搭配"]),

    ("词形转换", "工程学 engineering", "🔴", "练习册错题",
     "STEM refers to Science, Technology, ___ (engineer) and Maths.",
     ["engineer", "engineering", "engineers", "engineered"], "B",
     "STEM 指科学、技术、<strong>工程（学科）</strong>和数学，要用 engineering；engineer 是“工程师”，"
     "engineers 是其复数，engineered 是过去式，故选 B。",
     ["词形转换", "词义辨析", "engineering"]),

    ("词形转换", "形容词变名词 activity", "🟡", "练习册错题",
     "Playing chess and watching cartoons are indoor ___ (active).",
     ["activities", "active", "actives", "activitys"], "A",
     "active 是形容词“活跃的”，对应的名词是 activity“活动”，句中有 Playing 和 watching 两个并列动作，"
     "要用复数 activities；actives、activitys 都不是正确形式，故选 A。",
     ["词形转换", "形容词变名词", "复数"]),

    ("词形转换", "画家 artist", "🟡", "练习册错题",
     "The ___ (art) is preparing for his next painting.",
     ["art", "arts", "artist", "artistic"], "C",
     "正在画画的人是 <strong>artist</strong>“画家”；art 是“美术（学科）”，arts、artistic 都不合句意，"
     "故选 C。",
     ["词形转换", "名词变名词", "artist"]),

    ("词形转换", "名词复数 life→lives", "🟡", "练习册错题",
     "The text tells the amazing ___ (life) of different plants.",
     ["life", "lives", "lifes", "live"], "B",
     "life 的复数是<strong>不规则形式 lives</strong>；lifes、live 都不对，故选 B。",
     ["词形转换", "名词复数", "不规则复数"]),

    ("词形转换", "名词复数 comments", "🟢", "练习册错题",
     "These ___ (comment) are all from boys.",
     ["comments", "comment", "commented", "commenting"], "A",
     "these 后面的名词要用<strong>复数</strong>，comment 加 s 变 comments；commented 是过去式，"
     "commenting 是动名词，故选 A。",
     ["词形转换", "名词复数", "these"]),

    ("词形转换", "动词变名词 meeting", "🟡", "6A教材",
     "We have a class ___ (meet) every Monday afternoon.",
     ["meet", "meeting", "meets", "met"], "B",
     "meet 是动词「见面」，变名词「会议」要双写 t 再加 ing 变成 <strong>meeting</strong>；"
     "a class meeting 表示「一次班会／会议」，是 6A 校园生活中常用的说法。故选 B。",
     ["词形转换", "动词变名词", "meeting"]),

    ("词形转换", "形容词变副词 quickly", "🟡", "6A教材",
     "Please write down the answer ___ (quick) in your notebook.",
     ["quick", "quicker", "quickly", "quickest"], "C",
     "修饰动词 write down 要用<strong>副词</strong>。quick 是形容词「快的」，变副词直接加 -ly 变成 "
     "<strong>quickly</strong>；quicker 是比较级，quickest 是最高级，都不能直接修饰动词。故选 C。",
     ["词形转换", "形容词变副词", "quickly"]),

    ("词形转换", "different from", "🟡", "练习册错题",
     "My bedroom is ___ (different) ___ my twin sister Lily's.",
     ["different; from", "different; to", "difference; from", "different; than"], "A",
     "<strong>be different from</strong> 是固定搭配“与……不同”，第一空填形容词 different，第二空填介词 from；"
     "than 只用于比较句，故选 A。",
     ["词形转换", "固定搭配", "介词搭配"]),

    ("词形转换", "动词变名词 teacher", "🟢", "6A教材",
     "Miss Wang is our English ___ (teach).",
     ["teach", "teaching", "teacher", "taught"], "C",
     "teach 是动词“教”，指“教书的人”要用名词 <strong>teacher</strong>；teaching 是动名词，"
     "taught 是过去式，故选 C。",
     ["词形转换", "动词变名词", "teacher"]),

    ("词形转换", "形容词变副词 carefully", "🟡", "6A教材",
     "Please listen to the teacher ___ (careful).",
     ["careful", "carefulness", "care", "carefully"], "D",
     "修饰动词 listen 要用<strong>副词</strong> carefully“仔细地”；careful 是形容词，"
     "carefulness 是名词，care 是“关心”，故选 D。",
     ["词形转换", "形容词变副词", "carefully"]),

    ("词形转换", "名词变形容词 friendly", "🟡", "6A教材",
     "Our new English teacher is very ___ (friend) to us.",
     ["friend", "friendship", "friendly", "friendless"], "C",
     "<strong>be friendly to sb.</strong> 是固定搭配“对某人友好”，要用形容词 friendly；friend 是名词“朋友”，"
     "friendship 是“友谊”，friendless 是“无朋友的”，故选 C。",
     ["词形转换", "名词变形容词", "friendly"]),

    ("词形转换", "形容词 interesting", "🟡", "6A教材",
     "The story about our school life is very ___ (interest).",
     ["interest", "interested", "interestly", "interesting"], "D",
     "interesting /ˈɪntrəstɪŋ/ 修饰事物（the story）“有趣的”；interested 修饰人“我对……感兴趣”，"
     "interest 是名词“兴趣”，interestly 不是单词，故选 D。",
     ["词形转换", "名词变形容词", "interesting"]),

    ("词形转换", "名词变形容词 healthy", "🟢", "6A教材",
     "Eating vegetables keeps you ___ (health).",
     ["health", "healthily", "healthful", "healthy"], "D",
     "<strong>keep sb. healthy</strong> 是“使某人健康”，要用形容词 healthy；health 是名词“健康”，"
     "healthily 是副词，healthful 很少用，故选 D。",
     ["词形转换", "名词变形容词", "healthy"]),

    ("词形转换", "名词变名词 scientist", "🟡", "6A教材",
     "She wants to be a ___ (science) in the future.",
     ["science", "scientific", "scientist", "scientifics"], "C",
     "“科学家”是 <strong>scientist</strong>；science 是“科学”这门学科，scientific 是形容词“科学的”，"
     "scientifics 不是词，故选 C。",
     ["词形转换", "名词变名词", "scientist"]),

    ("词形转换", "副词变形容词 usual", "🟡", "6A教材",
     "It's ___ (usually) for us to have a class meeting on Monday morning.",
     ["usually", "usual", "unusually", "usefully"], "B",
     "usual /ˈjuːʒuəl/ 是形容词“通常的”，usually 是副词；<strong>It's usual for sb. to do sth.</strong> "
     "表示“某人通常做某事”，故选 B。",
     ["词形转换", "副词变形容词", "usual"]),

    ("词形转换", "动词第三人称单数 loves", "🟢", "练习册错题",
     "Everyone in our class ___ (love) the new school life.",
     ["love", "loving", "loved", "loves"], "D",
     "everyone 作主语要当成<strong>第三人称单数</strong>，一般现在时动词加 s，故选 D。",
     ["词形转换", "第三人称单数", "everyone"]),

    # ==================== 名词与数词（10） ====================
    ("名词与数词", "much 与 many 辨析", "🟡", "文来9月考",
     "There isn't ___ (much) water in the bottle, and there aren't ___ (many) students in the playground now.",
     ["much; many", "many; much", "much; much", "many; many"], "A",
     "water 是<strong>不可数名词</strong>，用 much；students 是可数名词复数，用 many，故选 A。",
     ["可数与不可数", "much", "many"]),

    ("名词与数词", "名词复数一般加 s", "🟢", "6AU1知识单",
     "There are two ___ (club) in our school: the Science Club and the English Club.",
     ["club", "clubs", "clubes", "clubing"], "B",
     "club 是普通名词，作“俱乐部”讲时直接加 s 变 <strong>clubs</strong>；clubes、clubing 都不是正确形式，"
     "故选 B。",
     ["名词复数", "一般加s", "6AU1"]),

    ("名词与数词", "辅音+y 变 ies", "🟡", "6AU1知识单",
     "There are many ___ (city) in China, and Shanghai is one of them.",
     ["city", "citys", "cities", "citis"], "C",
     "city 是“辅音字母 + y”结尾，复数<strong>去 y 加 ies</strong>，即 cities；citys、citis 都是常见错写，"
     "故选 C。",
     ["名词复数", "辅音+y", "cities"]),

    ("名词与数词", "不规则复数 children", "🟡", "6AU1知识单",
     "The teacher is talking with two ___ (child) in the playground.",
     ["child", "childs", "childrens", "children"], "D",
     "child 的复数是<strong>不规则形式 children</strong>；childs、childrens 都不是正确写法，故选 D。",
     ["名词复数", "不规则复数", "children"]),

    ("名词与数词", "不规则复数 teeth", "🟡", "6A教材",
     "I brush my ___ (tooth) twice a day.",
     ["teeth", "tooth", "tooths", "toothies"], "A",
     "tooth 的复数是<strong>不规则形式 teeth</strong>；tooths、toothies 都不是正确写法，故选 A。",
     ["名词复数", "不规则复数", "teeth"]),

    ("名词与数词", "单数名词的所有格", "🟡", "6AU1知识单",
     "Yesterday I found ___ (boy) pencil box under his desk.",
     ["boy", "boys", "boy's", "boys'"], "C",
     "单数名词所有格在 boy 后加 <strong>'s</strong>，表示“这个男孩的”；boys' 是复数所有格，故选 C。",
     ["名词所有格", "单数", "boy's"]),

    ("名词与数词", "复数名词的所有格", "🟡", "6AU1知识单",
     "These are the ___ (student) own books, not mine.",
     ["student", "students", "student's", "students'"], "D",
     "复数名词所有格在 students 后只加 <strong>'</strong>，表示“学生们各自的”；student's 是单数所有格，"
     "故选 D。",
     ["名词所有格", "复数", "students'"]),

    ("名词与数词", "易混名词 subject", "🟢", "6AU1知识单",
     "We have six ___ (subject) this term, and joining the Drama Club is a fun ___ (activity) after school.",
     ["subjects; activities", "subject; activities", "subjects; activity", "subject; activity"], "A",
     "subject 是“学科、科目”，<strong>本学期有六门</strong>要用复数 subjects；activity 是“活动”，"
     "joining ... 后面还有 after school，也要用复数 activities，故选 A。",
     ["名词辨析", "subject", "activity"]),

    ("名词与数词", "校园生活名词辨析", "🔴", "6AU1知识单",
     "Our English teacher put up the ___ (instruction) on the ___ (noticeboard), so we can see today's ___ (timetable) there too.",
     ["instruction; timetable; noticeboard", "instruction; noticeboard; timetable",
      "instructions; noticeboard; timetable", "instruction; noticeboard; timetables"], "B",
     "三个空分别要填 6AU1 校园生活词汇：instruction“说明、指示”、noticeboard“公告栏”、"
     "timetable“课程表”，对号入座故选 B。",
     ["名词辨析", "6AU1", "noticeboard"]),

    ("名词与数词", "序数词 first", "🟡", "6A教材",
     "Our new term starts on the ___ (one) day of September.",
     ["one", "once", "first", "a"], "C",
     "表示日期顺序要用<strong>序数词 first</strong>（第一）；one 是基数词“一”，once 是“一次”，"
     "a 是“一个”，都不合句意，故选 C。",
     ["数词", "序数词", "日期"]),
]
