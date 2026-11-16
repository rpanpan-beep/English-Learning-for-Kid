# -*- coding: utf-8 -*-
"""
六年级英语每日刷题 —— 知识点讲解库（语法手册部分）
教材：沪教牛津版 6A（上海新教材 Unit 1–10）
用法：可查阅、可背诵；每条含 rule（规则）/ examples（例句）/ warn（易错）/ tip（口诀）
"""

K = [
    {
        "category": "冠词",
        "icon": "📌",
        "level": "🟢",
        "points": [
            {
                "name": "a vs an：看音不看字",
                "rule": "元音音素开头用 an，辅音音素开头用 a，判断依据是读音而不是拼写。",
                "examples": [
                    "an apple（/æ/ 是元音音素）",
                    "a university（/j/ 是辅音音素）",
                    "an hour（h 不发音）",
                ],
                "warn": "honest、hour 的 h 不发音，仍用 an；university 开头读 /j/，用 a。",
                "tip": "口诀：看音不看字。",
            },
            {
                "name": "球类运动前用零冠词",
                "rule": "play、do 等动词后面接球类运动名词时，中间不加 the。",
                "examples": [
                    "He likes playing football.",
                    "Let's play basketball after school.",
                ],
                "warn": "乐器前要加 the：play the guitar、play the piano。",
                "tip": "球类零冠词，乐器加 the。",
            },
            {
                "name": "the 表示特指与独一无二",
                "rule": "再次提到某物、说话双方都清楚指的是哪一个，或表示独一无二的事物时，用 the。",
                "examples": [
                    "I joined a robot club last term. The club is on the third floor.",
                    "The sun rises in the east.",
                    "This is my timetable. Please put it on the desk.",
                ],
                "warn": "第一次提到要用 a/an：I joined a robot club last term. 第一次不能写 the。",
                "tip": "特指、二选一、独一无二都用 the。",
            },
        ],
    },
    {
        "category": "代词",
        "icon": "👥",
        "level": "🟢",
        "points": [
            {
                "name": "形容词性与名词性物主代词",
                "rule": "形容词性物主代词（my / your / his / her / its / our / their）后面必须跟名词；名词性物主代词（mine / yours / his / hers / ours / theirs）单独使用。",
                "examples": [
                    "This is my timetable.",
                    "That book is mine.",
                    "They like listening to music when they do their homework.",
                ],
                "warn": "hers 是名词性，不能写成 her's；my 后面不能单独作主语，单独用要写 mine。",
                "tip": "后面有名词用 my/your/their，后面没名词用 mine/yours/theirs。",
            },
            {
                "name": "反身代词表示自己",
                "rule": "动作的承受者与主语是同一个人或物时，宾语要用反身代词。",
                "examples": [
                    "The students made the model robot by themselves.",
                    "He taught himself to swim.",
                    "Please help yourself to some fruit.",
                ],
                "warn": "反身代词不能作句子的主语，也不能放在 be 动词后面作表语，句子的主语必须是别人或别的事物。",
                "tip": "自己对自己，才用 himself / herself / themselves。",
            },
            {
                "name": "both、all 与 either",
                "rule": "both 表示两者都；all 表示三者以上都；either 表示两者中的任一个；neither 表示两者都不。",
                "examples": [
                    "Both of my parents are teachers.",
                    "All the students joined the activity.",
                    "Either club is fine for me.",
                ],
                "warn": "neither 本身已经含有否定的意思，不能再加 not。",
                "tip": "两者用 both / either / neither，三者以上用 all。",
            },
            {
                "name": "each other 的用法",
                "rule": "each other 多指两者互相，one another 多指三者以上互相。",
                "examples": [
                    "We should help each other at school.",
                    "The three new students help one another with their English.",
                ],
                "warn": "不要和 every other（每一个、每隔一个）混淆，every other day 是每隔一天。",
                "tip": "each other 谈两者，one another 谈三人以上。",
            },
        ],
    },
    {
        "category": "名词与数词",
        "icon": "🔢",
        "level": "🟢",
        "points": [
            {
                "name": "可数名词与不可数名词",
                "rule": "可数名词有复数形式，可以用 a/an 和数字修饰；不可数名词没有复数形式，也不能用 a/an 修饰。",
                "examples": [
                    "We have a lot of activities after school.",
                    "I need some information about the history exam.",
                ],
                "warn": "information、news、homework 都不可数，不能写 informations、newses，也不能加 a。",
                "tip": "能被数字数出来的才是可数名词。",
            },
            {
                "name": "名词复数的特殊变化",
                "rule": "辅音字母加 y 结尾的名词变复数时，去 y 加 ies；f / fe 结尾多变 ves；child、man 等属于不规则变化。",
                "examples": [
                    "There are two stories in the book.",
                    "Two leaves are on the desk.",
                    "The children are playing games.",
                ],
                "warn": "child 的复数是 children，不是 childs；story 的复数是 stories，不是 storys。",
                "tip": "辅音加 y：去 y 加 ies。",
            },
            {
                "name": "基数词与序数词的用法",
                "rule": "基数词表示数量；序数词表示顺序，前面通常加 the，句中作表语时用 be 动词。",
                "examples": [
                    "I have three pairs of shoes.",
                    "He came second in the singing competition.",
                    "My Chinese class finishes at 1:50.",
                ],
                "warn": "序数词 first 不能写成 one；序数词也不能加 s 变复数，如 twelfhs 是错的。",
                "tip": "顺序用序数词，前面别忘 the。",
            },
        ],
    },
    {
        "category": "介词",
        "icon": "📍",
        "level": "🟡",
        "points": [
            {
                "name": "时间介词 at / in / on",
                "rule": "at 用于具体时刻；in 用于较长的时间段（年、月、季节、上午下午）；on 用于具体某一天或某天的上午、下午、晚上。",
                "examples": [
                    "Classes start at 8:00 in the morning.",
                    "The film club meets on Tuesday afternoons.",
                    "We have a break in the morning.",
                ],
                "warn": "in the morning 用 in，但 on Monday morning 用 on。",
                "tip": "点用 at，天用 on，年月季节用 in。",
            },
            {
                "name": "地点介词 in / on / at",
                "rule": "at 用于小地点或具体位置；on 表示在表面上；in 表示在内部或较大的地点。",
                "examples": [
                    "We are in the science lab now.",
                    "Your book is on the desk.",
                    "Let's meet at the school gate at four.",
                ],
                "warn": "在教室里用 in the classroom，在操场上用 on the sports field。",
                "tip": "看位置：里面用 in，表面用 on，小点用 at。",
            },
            {
                "name": "固定介词搭配要背熟",
                "rule": "be good at、be interested in、be late for、be ready for、take part in 等都是固定搭配，介词不能换。",
                "examples": [
                    "She is interested in the robot club.",
                    "Don't be late for the first class.",
                    "He is good at English.",
                ],
                "warn": "be good at 后接名词或 doing，不能说 be good at to do。",
                "tip": "搭配要整块背，不要一个词一个词拼。",
            },
            {
                "name": "in + 语言与 by + 交通",
                "rule": "用某种语言说话用 in；乘交通工具用 by + 交通工具名词（不加冠词）。",
                "examples": [
                    "We have an English lesson and speak in English.",
                    "I go to school by bike.",
                ],
                "warn": "by bus / by car 不加 the；步行要说 on foot，不能说 by foot。",
                "tip": "语言用 in，交通用 by，步行用 on foot。",
            },
        ],
    },
    {
        "category": "时态·一般现在时",
        "icon": "⏰",
        "level": "🟢",
        "points": [
            {
                "name": "第三人称单数动词加 s",
                "rule": "一般现在时中，如果主语是第三人称单数，谓语动词要加 -s 或 -es。",
                "examples": [
                    "Mary plays the guitar on Sundays.",
                    "He watches TV after dinner.",
                    "My mother gets up early every day.",
                ],
                "warn": "play 变 plays，watch 变 watches，go 变 goes；不能写 playes 或 goos。",
                "tip": "三单变化只有三种：加 s、加 es、变 y 为 ies。",
            },
            {
                "name": "第三人称单数怎么判断",
                "rule": "人名、he / she / it、单个的人或物、不可数名词作主语时，动词用三单；主语是复数则用原形。",
                "examples": [
                    "Everyone loves this new club.",
                    "My friends play basketball after school.",
                    "The science club is open to everyone.",
                ],
                "warn": "everyone 看作单数，谓语用 enjoys，不能写 everyone enjoy。",
                "tip": "先看主语是谁、几个，再决定动词。",
            },
            {
                "name": "频率副词放在哪里",
                "rule": "always、usually、often、sometimes、never 等频率副词放在实义动词前面、be 动词后面。",
                "examples": [
                    "She often reads English books.",
                    "He is always late for class.",
                ],
                "warn": "不能说 She often is late.；也不能说 She reads often English books.。",
                "tip": "实义动词在前，be 动词在后。",
            },
            {
                "name": "一般现在时表客观真理",
                "rule": "科学事实、永远成立的道理用一般现在时，不用于进行时。",
                "examples": [
                    "The earth goes around the sun.",
                    "Light travels very fast.",
                ],
                "warn": "客观真理不用进行时，不能写 The earth is going around the sun.。",
                "tip": "永远成立 → 一般现在时。",
            },
        ],
    },
    {
        "category": "时态·现在进行时",
        "icon": "🏃",
        "level": "🟢",
        "points": [
            {
                "name": "be + 动词 -ing 结构",
                "rule": "现在进行时表示此刻正在进行的动作，由 am / is / are 加动词的 -ing 形式构成。",
                "examples": [
                    "Look! The girls are singing a song.",
                    "Nina is running on the sports field now.",
                ],
                "warn": "不能漏掉 be 动词，不能写 The girls singing a song.。",
                "tip": "看到 Look!、Listen!、now，就用进行时。",
            },
            {
                "name": "动词加 -ing 的拼写变化",
                "rule": "以不发音的 e 结尾的动词，去掉 e 再加 ing；重读闭音节且末尾是单个辅音字母的动词，要双写该字母再加 ing。",
                "examples": [
                    "We are making a mini volcano.",
                    "He is running on the sports field.",
                    "They are taking photos in the lab.",
                ],
                "warn": "make 变 making（去 e），run 变 running（双写 n），write 变 writing（去 e）。",
                "tip": "去 e 加 ing，双写后加 ing。",
            },
            {
                "name": "进行时与一般现在时的区别",
                "rule": "句中有 now、Look!、Listen! 等标志词用现在进行时；表示经常发生的习惯用一般现在时。",
                "examples": [
                    "Look! My little brother is playing with his toys.",
                    "He usually puts his toys neatly in the box before going to bed.",
                ],
                "warn": "不能写 Look! My little brother plays with his toys.。",
                "tip": "先找标志词，再定时态。",
            },
            {
                "name": "be 动词与主语一致",
                "rule": "现在进行时中，I 用 am，he / she / it 和单数名词用 is，you / we / they 和复数名词用 are。",
                "examples": [
                    "I am reading a story now.",
                    "They are playing football on the sports field.",
                ],
                "warn": "主语是复数就要用 are，不能写 The students is singing.。",
                "tip": "我用 am，你用 are，is 连着他她它。",
            },
        ],
    },
    {
        "category": "时态·一般过去时",
        "icon": "⏮",
        "level": "🟡",
        "points": [
            {
                "name": "动词过去式的变化",
                "rule": "一般过去时用动词的过去式；规则动词加 -ed，不规则动词要单独记牢。",
                "examples": [
                    "We went to the Great Wall last Sunday.",
                    "He watched TV last night.",
                    "They had a good time at the party.",
                ],
                "warn": "go 的过去式是 went，不是 goed；watch 的过去式是 watched，不是 watchd。",
                "tip": "不规则动词表要常翻常背。",
            },
            {
                "name": "be 动词的过去式",
                "rule": "am / is 的过去式是 was，are 的过去式是 were；单数主语用 was，复数主语用 were。",
                "examples": [
                    "Her hair was short and her eyes were big.",
                    "The film was wonderful.",
                    "My hands were small then.",
                ],
                "warn": "主语是复数要用 were，不能写 My hands was small then.。",
                "tip": "过去式只有两个：was、were。",
            },
            {
                "name": "过去时的时间标志词",
                "rule": "yesterday、last night、last week、two days ago、in 2020 等词提示动作发生在过去。",
                "examples": [
                    "I visited my grandparents last Sunday.",
                    "We didn't watch TV last night.",
                ],
                "warn": "ago 只能和过去时连用，不能写 two days ago I will call you.。",
                "tip": "看到 last / yesterday / ago 就用过去时。",
            },
            {
                "name": "过去时的否定与疑问",
                "rule": "否定句在实义动词前加 didn't；疑问句把 did 提到句首，动词一律还原成原形。",
                "examples": [
                    "I didn't go to the cinema yesterday.",
                    "Did you join the club last term?",
                    "Did she have a good time?",
                ],
                "warn": "用了 did，后面的动词必须还原，不能写 Did you went to the club?。",
                "tip": "did 一出现，动词回原形。",
            },
        ],
    },
    {
        "category": "时态·一般将来时",
        "icon": "⏭",
        "level": "🟡",
        "points": [
            {
                "name": "be going to 表打算",
                "rule": "be going to + 动词原形，表示已经打算好、计划好要做的某事。",
                "examples": [
                    "My mother is going to buy some groceries this afternoon.",
                    "We are going to have a sports meeting next week.",
                ],
                "warn": "going 后面必须接动词原形，不能写 is going to bought.。",
                "tip": "打算做某事 → going to do。",
            },
            {
                "name": "will 表将来",
                "rule": "will + 动词原形，表示将来某时要发生的动作，或临时作出的决定。",
                "examples": [
                    "I will call you after school.",
                    "Don't worry. I will help you with your project.",
                ],
                "warn": "will 后面只能接动词原形，不能写 will to do 或 will going to do.。",
                "tip": "临时决定用 will do。",
            },
            {
                "name": "将来时的常见标志词",
                "rule": "tomorrow、next week、next term、in three days 等表示将来的时间。",
                "examples": [
                    "We are going to visit the museum next Friday.",
                    "I am going to see a film this weekend.",
                ],
                "warn": "next 前面不加介词，不能说 in next week，应说 next week。",
                "tip": "next 前不加 in，in + 一段时间表多久以后。",
            },
        ],
    },
    {
        "category": "情态动词",
        "icon": "🔑",
        "level": "🟢",
        "points": [
            {
                "name": "can 表示能力与请求",
                "rule": "can + 动词原形，表示有能力做某事，也可用于礼貌地提出请求。",
                "examples": [
                    "I can play the guitar well.",
                    "Can you show me your new timetable?",
                ],
                "warn": "can 没有人称和数的变化，不能写 cans 或 can to play.。",
                "tip": "can 后面永远跟动词原形。",
            },
            {
                "name": "must 表示必须",
                "rule": "must + 动词原形，表示必须做某事；否定式 mustn't 表示禁止做某事。",
                "examples": [
                    "We must follow the instructions on the school noticeboard.",
                    "You mustn't run in the school hall.",
                ],
                "warn": "否定用 mustn't 表示禁止，不要写 don't must.；「不必」才用 don't have to.。",
                "tip": "mustn't 是禁止，don't have to 是不必。",
            },
            {
                "name": "should 表示应该",
                "rule": "should + 动词原形，表示应该做某事、提出建议。",
                "examples": [
                    "You should join the science club.",
                    "We should read the instructions carefully.",
                ],
                "warn": "should 后面接动词原形，不加 to，不能写 should to take part in.。",
                "tip": "提建议用 should do。",
            },
            {
                "name": "may 与 might 表许可可能",
                "rule": "may / might + 动词原形，may 表示许可和请求，might 表示可能性。",
                "examples": [
                    "May I use your dictionary?",
                    "The film club might be open to Grade 6 students.",
                ],
                "warn": "May I 开头的请求句要用疑问语调，后面接动词原形，不能写 May I using it?。",
                "tip": "May I …? 是最礼貌的请求句式。",
            },
        ],
    },
    {
        "category": "词型结构·to do 与 doing",
        "icon": "🎯",
        "level": "🟡",
        "points": [
            {
                "name": "want 等动词后接 to do",
                "rule": "want、hope、plan、decide、agree、promise 等动词后接 to do sth.，表示打算做某事。",
                "examples": [
                    "I want to join the AI club.",
                    "We plan to take part in the English Festival.",
                    "She decided to learn swimming.",
                ],
                "warn": "这些动词后面不能接 doing，不能写 I want joining the club.。",
                "tip": "want / hope / plan / decide + to do。",
            },
            {
                "name": "enjoy 等动词后接 doing",
                "rule": "enjoy、finish、mind、practice、keep、suggest 等动词后接 doing sth.。",
                "examples": [
                    "I enjoy playing football with my friends.",
                    "Would you mind opening the window?",
                    "She finished reading the story book.",
                ],
                "warn": "不能说 I enjoy to play football.，也不能说 Would you mind to open the window?。",
                "tip": "enjoy / finish / mind / practise + doing。",
            },
            {
                "name": "remember 的两种用法",
                "rule": "remember、forget 后接 to do 指还没做的事，接 doing 指已经做过的事；stop to do 是停下来去做另一件事，stop doing 是停下手上的事。",
                "examples": [
                    "Remember to close the door when you leave.",
                    "I remember meeting her last year.",
                    "He stopped to buy a newspaper.",
                ],
                "warn": "stop doing 与 stop to do 意思完全不同，stop doing 是「不再做」，stop to do 是「改做别的」。",
                "tip": "to do 还没做，doing 已经做过。",
            },
        ],
    },
    {
        "category": "词型结构·宾语+动词原形",
        "icon": "🧩",
        "level": "🟡",
        "points": [
            {
                "name": "let 等使役动词省 to",
                "rule": "let、make、have 等使役动词后面接「宾语 + 动词原形」，不定式符号 to 必须省略。",
                "examples": [
                    "Let me help you with your bags.",
                    "Let Ken show you his new timetable.",
                    "I'll have my brother help you.",
                ],
                "warn": "let 后面不能写 to，不能说 Let me to help you.。",
                "tip": "let / make / have 后面 to 一定省掉。",
            },
            {
                "name": "ask 等动词接 sb. to do",
                "rule": "ask、want、need、tell、teach、invite、remind 等动词后面接「宾语 + to do sth.」。",
                "examples": [
                    "She asked me to help her with the project.",
                    "We need you to finish it today.",
                    "He told me to wait outside.",
                ],
                "warn": "ask 后面要带 to，不能写 She asked me help her.。",
                "tip": "ask / want / need / tell + 人 + to do。",
            },
            {
                "name": "感官动词 + 宾语 + 原形",
                "rule": "see、hear、watch、notice、feel 等感官动词后接「宾语 + 动词原形」，表示看见或听见动作的全过程。",
                "examples": [
                    "I saw him cross the street.",
                    "I noticed him put down his schoolbag.",
                    "My teacher watched us do the experiment.",
                ],
                "warn": "感官动词后面不能加 to，不能写 I saw him to cross the street.。",
                "tip": "看到听到全过程 → 用原形。",
            },
            {
                "name": "help sb. (to) do",
                "rule": "help 后面接「宾语 + (to) do sth.」，to 可以写也可以省略，两种都对。",
                "examples": [
                    "Could you help me (to) find my pen?",
                    "He helped me clean the room.",
                ],
                "warn": "help 后的 to 不能丢，但写成 helped me clean 也是对的，不要和 let 混在一起记。",
                "tip": "help 最宽容，to 写不写都行。",
            },
        ],
    },
    {
        "category": "词型结构·be 动词结构",
        "icon": "🧱",
        "level": "🟢",
        "points": [
            {
                "name": "be 动词的三种形式",
                "rule": "am 用在 I 后面；is 用在 he / she / it 和单数名词后面；are 用在 you / we / they 和复数名词后面。",
                "examples": [
                    "I am in Grade 6.",
                    "He is my classmate.",
                    "They are on the sports field now.",
                ],
                "warn": "主语是复数用 are，不能写 My friends is my classmate.。",
                "tip": "我 am 你 are，is 连着他她它。",
            },
            {
                "name": "be 动词的否定",
                "rule": "否定句在 be 动词后面加 not，口语中常缩写为 isn't、aren't、I'm not。",
                "examples": [
                    "She is not in the science lab now.",
                    "They aren't playing football now.",
                ],
                "warn": "缩写形式后面不能再加 be，不能写 She isn't be here.。",
                "tip": "否定就在 be 后面加 not。",
            },
            {
                "name": "be 动词的一般疑问句",
                "rule": "把 be 动词提到句首，句子其余部分保持不变，就变成一般疑问句。",
                "examples": [
                    "Are you ready?",
                    "Is there a lot of water on the table?",
                ],
                "warn": "疑问句中主语后面不再重复 be，不能写 Are you are ready?。",
                "tip": "be 提到句首就是疑问句。",
            },
            {
                "name": "be 动词后的表语",
                "rule": "be 动词后面接形容词、名词或介词短语作表语，说明主语是什么或怎么样。",
                "examples": [
                    "The film club is open to Grade 6 students.",
                    "My favourite subject is PE.",
                    "Miss Lin is tall and friendly.",
                ],
                "warn": "be 后面不能直接跟动词原形，不能写 The club is make films.。",
                "tip": "be 后面接名词或形容词。",
            },
        ],
    },
    {
        "category": "词型结构·动词+副词",
        "icon": "🧰",
        "level": "🟡",
        "points": [
            {
                "name": "代词宾语必须放中间",
                "rule": "短语动词（动词 + 副词）后接代词作宾语时，代词必须放在动词和副词中间。",
                "examples": [
                    "Put everything in your bag and then take them out on the desk.",
                    "Look at the blackboard carefully.",
                    "Take off your shoes before you enter the science lab.",
                ],
                "warn": "代词不能放在短语动词后面，不能写 take out them.。",
                "tip": "代词放中间：take them out。",
            },
            {
                "name": "常用动词加副词短语",
                "rule": "take a break、take part in、put on、put away、turn on、turn off 等是固定搭配，要整块记忆。",
                "examples": [
                    "Let's take a break after the third class.",
                    "Students can take part in the singing competition.",
                    "Put on your coat before you go out.",
                ],
                "warn": "take part in 后面必须有 in，不能说 take part the competition.。",
                "tip": "整块背，别拆开单背动词。",
            },
            {
                "name": "off 的常见意思",
                "rule": "put off 推迟，put on 穿上，put away 收好，get off 下车，get on 上车，turn off 关掉。",
                "examples": [
                    "They put off the sports meeting to Friday.",
                    "Get off at the next stop.",
                    "Please turn off the light before you leave.",
                ],
                "warn": "put off 是推迟不是穿上，穿上要用 put on；take off 是脱下衣服。",
                "tip": "off 多表示离开、关掉、推迟。",
            },
        ],
    },
    {
        "category": "双宾语",
        "icon": "🎁",
        "level": "🟡",
        "points": [
            {
                "name": "give sb. sth. 的语序",
                "rule": "give、pass、show、send、bring、lend、buy 等动词后面可以接两个宾语，顺序是先人后物。",
                "examples": [
                    "Please give the book back to me.",
                    "Can you show me your new timetable?",
                    "He gave his sister a beautiful present.",
                ],
                "warn": "两个宾语的顺序不能颠倒，不能写 give the book me.。",
                "tip": "先人后物：give me the book。",
            },
            {
                "name": "给某人做某物用 for",
                "rule": "buy、make、cook、get、order 等动词表示「给某人做/买某物」时，用 for sb.，不用双宾语。",
                "examples": [
                    "I'll buy a notebook for you.",
                    "My mother made a cake for me.",
                ],
                "warn": "介词要用 for，不能写 buy a notebook to me.。",
                "tip": "give 用双宾语，buy / make 用 for。",
            },
            {
                "name": "双宾语与介词短语的转换",
                "rule": "双宾语结构可以改写成「动词 + 介词 + 物」的形式，改写时两个宾语合并成一个。",
                "examples": [
                    "He gave his sister a present. → He gave a present to his sister.",
                    "Please show the ticket to the teacher.",
                ],
                "warn": "转换时是物 + 介词 + 人，不是人 + 介词 + 物。",
                "tip": "两个宾语 → 一个物 + 介词 + 人。",
            },
        ],
    },
    {
        "category": "There be",
        "icon": "🏠",
        "level": "🟢",
        "points": [
            {
                "name": "there be 句型的就近原则",
                "rule": "there be 表示「有」，be 动词与离它最近的那个名词保持一致，这就是就近原则。",
                "examples": [
                    "There is a lot of water on the ground.",
                    "There are two English books and a pencil on the desk.",
                ],
                "warn": "不可数名词后用 is，不能写 There are some waters.；也不要写成 There is some waters.。",
                "tip": "就近原则，就近看名词。",
            },
            {
                "name": "there be 与 have 辨析",
                "rule": "there be 表示某处有某物，have 表示某人拥有某物，二者不能混用。",
                "examples": [
                    "There is a poster on the noticeboard.",
                    "We have seven classes every day.",
                ],
                "warn": "不能说 There have a poster on the wall.，也不能说 We have there a poster.。",
                "tip": "某处有 → there be；某人拥有 → have。",
            },
            {
                "name": "there be 的否定与疑问",
                "rule": "否定在 be 后面加 not；疑问句把 be 提到 there 前面，同时 some 要改成 any。",
                "examples": [
                    "There isn't any water in the bottle.",
                    "Are there any students in the lab?",
                ],
                "warn": "否定句和疑问句中 some 要变成 any，不能写 Are there some students in the lab?。",
                "tip": "否定、疑问句中 some 变 any。",
            },
            {
                "name": "表示「有……时间段」的搭配",
                "rule": "表示某人拥有某段时间用 have，表示某处存在某段时间用 there be。",
                "examples": [
                    "We have a 10-minute break between classes.",
                    "There is a ten-minute break between classes.",
                    "The 3D printing club is from 16:00 to 17:00 on Wednesday.",
                ],
                "warn": "两种说法不能混用，不能写 There have a break between classes.。",
                "tip": "处所有用 there be，人有才用 have。",
            },
        ],
    },
    {
        "category": "祈使句",
        "icon": "📢",
        "level": "🟢",
        "points": [
            {
                "name": "祈使句以动词原形开头",
                "rule": "祈使句表示请求、命令或建议，句子直接以动词原形开头，不写主语。",
                "examples": [
                    "Open your computer, please.",
                    "Turn left at the second corner.",
                ],
                "warn": "祈使句不能加主语，不能写 You open the computer.。",
                "tip": "动词原形打头阵。",
            },
            {
                "name": "祈使句的否定形式",
                "rule": "否定祈使句在句首加 Don't，后面仍用动词原形。",
                "examples": [
                    "Don't be late for class.",
                    "Don't run in the school hall.",
                ],
                "warn": "不要写成 Don't you be late.；否定祈使句后面也不需要加 be。",
                "tip": "Don't + 动词原形。",
            },
            {
                "name": "Let's 引导的祈使句",
                "rule": "Let's + 动词原形，表示提议大家一起做某事；否定形式是 Let's not。",
                "examples": [
                    "Let's make our films together!",
                    "Let's take a break.",
                ],
                "warn": "Let's 后面接动词原形，不能写 Let's to make films.。",
                "tip": "Let's + 原形，一起做。",
            },
            {
                "name": "祈使句加 please 更礼貌",
                "rule": "在祈使句的句首或句尾加 please，语气会更礼貌；放在句首时后面要加逗号。",
                "examples": [
                    "Please follow the instructions.",
                    "Close the door, please.",
                ],
                "warn": "please 放在句首时要加逗号，不能写 Please, open the door.。",
                "tip": "please 加逗号才礼貌。",
            },
        ],
    },
    {
        "category": "主谓一致",
        "icon": "⚖️",
        "level": "🟡",
        "points": [
            {
                "name": "第三人称单数主语",
                "rule": "主语是第三人称单数时，谓语动词必须用三单形式。",
                "examples": [
                    "Everyone loves this new club.",
                    "My mother gets up early every day.",
                ],
                "warn": "everyone 是单数，不能写 everyone love this club.。",
                "tip": "谁做主语，就看谁的数量。",
            },
            {
                "name": "复数主语用动词原形",
                "rule": "主语是复数名词或 they 时，谓语动词用原形；不可数名词作主语时用单数。",
                "examples": [
                    "My friends play basketball after school.",
                    "Homework is difficult for me.",
                ],
                "warn": "不可数名词作主语用单数，不能写 Homework are difficult.。",
                "tip": "先判主语单复数，再定动词。",
            },
            {
                "name": "each 与 every 后接单数",
                "rule": "each 和 every 作主语时一律看作单数，后面的名词也用单数。",
                "examples": [
                    "Each student has a new timetable.",
                    "Every club member gets a badge.",
                ],
                "warn": "不能说 Each students have a new timetable.，也不能说 Every club members get a badge.。",
                "tip": "each / every 后面永远单数。",
            },
        ],
    },
    {
        "category": "疑问词",
        "icon": "❓",
        "level": "🟢",
        "points": [
            {
                "name": "What is like 与 How",
                "rule": "问「……怎么样」的评价用 What is ... like?；问「怎样（方式）」才用 How。",
                "examples": [
                    "What is your school day like? — It's great.",
                    "How do you remember new English words? — By using a dictionary.",
                ],
                "warn": "问「你的学校一天怎么样」要用 What is ... like?，不能用 How is your school day like?。",
                "tip": "What is ... like? 问评价，How 问方式。",
            },
            {
                "name": "many 与 much 的区别",
                "rule": "How many 提问可数名词的数量，How much 提问不可数名词的数量或价钱。",
                "examples": [
                    "How many clubs do you have on your timetable?",
                    "How much water is there in the bottle?",
                    "How many activities can you take part in?",
                ],
                "warn": "不可数名词只能用 How much，不能用 How many。",
                "tip": "可数 many，不可数 much。",
            },
            {
                "name": "频率与时长的提问",
                "rule": "How often 提问频率（多久一次），How long 提问时间长度或物体的长度。",
                "examples": [
                    "How often do you go to the library? — Twice a week.",
                    "How long do you stay at the club? — For two hours.",
                ],
                "warn": "问频率用 How often，问多长时间用 How long，二者不能互换。",
                "tip": "often 问频率，long 问时长。",
            },
            {
                "name": "特殊疑问词三兄弟",
                "rule": "Whose 问「谁的」，Which 在有限范围内问「哪一个」，What 问「什么」。",
                "examples": [
                    "Whose schoolbag is under the desk? — It's mine.",
                    "Which is your favourite subject, Maths or English?",
                    "What's the meaning of this new word?",
                ],
                "warn": "给出两个具体选项时要用 Which，不能用 What。",
                "tip": "二选一用 Which，问主人用 Whose。",
            },
        ],
    },
    {
        "category": "句型转换",
        "icon": "🔄",
        "level": "🟡",
        "points": [
            {
                "name": "一般现在时的否定与疑问",
                "rule": "否定句用 don't / doesn't + 动词原形；疑问句把 don't / does 提到句首，动词还原成原形。",
                "examples": [
                    "My parents don't take me to the park at weekends.",
                    "Does Tom often play basketball after school?",
                ],
                "warn": "用了 doesn't，动词必须还原，不能写 Doesn't he plays basketball?。",
                "tip": "do / does 一出现，动词回原形。",
            },
            {
                "name": "划线提问的三个步骤",
                "rule": "先看划线部分表示什么，再选相应的疑问词，最后把疑问词和助动词放到句首。",
                "examples": [
                    "Our first class starts at 8:10. → When does your first class start?",
                    "Her favourite subject is Geography. → What is her favourite subject?",
                    "I have three pairs of shoes. → How many pairs of shoes do you have?",
                ],
                "warn": "问时间用 When，问数量用 How many，问具体事物用 What，不能混用。",
                "tip": "先看划线是什么，再选疑问词。",
            },
            {
                "name": "改写后句意必须不变",
                "rule": "句型转换只改说法，不改句子的核心意思。",
                "examples": [
                    "I'm good at playing football. → I am also good at playing football.",
                    "She doesn't have PE lessons. → She doesn't have PE lessons on her timetable.",
                ],
                "warn": "把 I'm good at playing football 改成 How are you? 是错的，句意已经完全变了。",
                "tip": "改写前后意思必须一致。",
            },
        ],
    },
    {
        "category": "形容词比较级",
        "icon": "📊",
        "level": "🟢",
        "points": [
            {
                "name": "单音节词加 er / est",
                "rule": "一般单音节形容词比较级加 -er，最高级加 -est；重读闭音节要双写末尾辅音字母。",
                "examples": [
                    "tall → taller → tallest",
                    "big → bigger → biggest",
                    "young → younger → youngest",
                ],
                "warn": "big 要双写 g，不能写 biger；good 的比较级是 better，不是 gooder。",
                "tip": "重读闭音节，双写末尾字母再加 er。",
            },
            {
                "name": "多音节词用 more / most",
                "rule": "两个音节以上的形容词，比较级用 more，最高级用 most。",
                "examples": [
                    "more useful",
                    "the most difficult",
                    "more carefully",
                ],
                "warn": "不能说 more tallest；最高级前要加 the 或形容词性物主代词。",
                "tip": "长词用 more / most，短词用 -er / -est。",
            },
            {
                "name": "不规则比较级要单记",
                "rule": "good / well → better → best；bad / ill → worse → worst；many / much → more → most。",
                "examples": [
                    "Maths is easier than English.",
                    "I have more free time than you.",
                    "Of all the subjects, Science is the most interesting.",
                ],
                "warn": "many / much 的比较级是 more，不能写 manier；bad 的比较级是 worse，不是 badder。",
                "tip": "好—更好—最好：better / best。",
            },
            {
                "name": "最高级要说出范围",
                "rule": "比较两者用 than；比较三者以上要用 in 或 of 引导出比较的范围。",
                "examples": [
                    "Tom is taller than Jack.",
                    "Of all the sports, basketball is the most exciting for me.",
                ],
                "warn": "最高级一定要有比较范围，不能只写 the most exciting sport。",
                "tip": "最高级别忘了范围。",
            },
        ],
    },
    {
        "category": "复合形容词",
        "icon": "🧷",
        "level": "🟢",
        "points": [
            {
                "name": "数词加名词作定语",
                "rule": "数词和名词同时修饰另一个名词时，中间加连字符，名词用单数形式。",
                "examples": [
                    "a ten-minute break",
                    "a five-minute walk",
                    "a two-week reading plan",
                ],
                "warn": "作定语时名词用单数，不能写 a ten-minutes break；连字符不能漏。",
                "tip": "连字符连接，数词在前名词单数。",
            },
            {
                "name": "形容词加名词作定语",
                "rule": "复合形容词一般由形容词加名词构成，前面只加一个冠词，名词前不再加 a 或 the。",
                "examples": [
                    "a new classmate",
                    "a science club",
                    "a PE teacher",
                ],
                "warn": "只能加一个冠词，不能写 a new the classmate。",
                "tip": "一个名词，一个冠词。",
            },
            {
                "name": "介词短语作后置定语",
                "rule": "形容词后面接介词短语作定语时，这个定语要放在名词后面。",
                "examples": [
                    "the students in Grade 6",
                    "the club on the third floor",
                    "a book for reading",
                ],
                "warn": "介词短语作定语必须后置，不能写成 in the Grade 6 students。",
                "tip": "定语太长就放后面。",
            },
        ],
    },
    {
        "category": "连词",
        "icon": "🔗",
        "level": "🟢",
        "points": [
            {
                "name": "and / but / or 连接",
                "rule": "and 表示并列，but 表示转折，or 表示选择，用它们连接两个句子或两个短语。",
                "examples": [
                    "I want to join the science club, but I have no time on Friday.",
                    "You can take the bus or the underground.",
                ],
                "warn": "两个完整句子不能只用逗号连接，必须用连词或句号，不能写成 I like music, I like PE.。",
                "tip": "逗号加连词，句子才不断开。",
            },
            {
                "name": "because 引导原因",
                "rule": "because 引出原因状语从句，回答 Why 的问题。",
                "examples": [
                    "I like Science because I can do some experiments in the lab.",
                    "She joined the art club because she likes drawing.",
                ],
                "warn": "because 和 so 不能同时出现在一个句子里。",
                "tip": "因为用 because，所以用 so。",
            },
            {
                "name": "so 引导结果状语",
                "rule": "so 引出结果，回答 What happens 的问题。",
                "examples": [
                    "Three hours of study is too long, so I need to take a short break.",
                    "It was raining, so we stayed at home.",
                ],
                "warn": "so 和 but 不能同时出现在一个句子里。",
                "tip": "一因一果，because 和 so 只能选一个。",
            },
        ],
    },
    {
        "category": "语音·元音辨音",
        "icon": "🔊",
        "level": "🟡",
        "points": [
            {
                "name": "闭音节要读短元音",
                "rule": "辅音字母加元音字母加辅音字母构成的闭音节中，元音字母读短音。",
                "examples": [
                    "cat /kæt/",
                    "desk /desk/",
                    "hot /hɒt/",
                ],
                "warn": "desk 中 e 读 /e/，不是 /iː/；hot 中 o 读 /ɒ/，不是 /əʊ/。",
                "tip": "闭音节读短音。",
            },
            {
                "name": "开音节读字母本音",
                "rule": "元音字母加辅音字母加 e 构成的开音节中，元音字母读字母本身的音。",
                "examples": [
                    "name /neɪm/",
                    "he /hiː/",
                    "note /nəʊt/",
                ],
                "warn": "have、give、like 中的 a/e 是短音，不能一律套用开音节规则。",
                "tip": "开音节读字母音。",
            },
            {
                "name": "同一字母的不同读音",
                "rule": "同一个字母在不同单词中可能读不同的音，必须结合音标逐词记忆。",
                "examples": [
                    "know /nəʊ/, now /naʊ/, how /haʊ/",
                    "photo /ˈfəʊtəʊ/, open /ˈəʊpən/",
                ],
                "warn": "know 读 /əʊ/，now、how、cow 读 /aʊ/；photo 的 o 读 /əʊ/，hot 的 o 读 /ɒ/。",
                "tip": "背单词一定连音标一起背。",
            },
        ],
    },
    {
        "category": "语音·辅音与重音",
        "icon": "🎵",
        "level": "🟡",
        "points": [
            {
                "name": "清辅音和浊辅音配对",
                "rule": "清辅音发音时声带不振动，浊辅音发音时声带振动；s/z、f/v、θ/ð、p/b 是常见成对辅音。",
                "examples": [
                    "sink /sɪŋk/ — zinc /zɪŋk/",
                    "safe /seɪf/ — save /seɪv/",
                    "think /θɪŋk/ — thing /ðɪŋ/",
                ],
                "warn": "think 用清辅音 /θ/，thing 用浊辅音 /ð/，两个词发音完全不同。",
                "tip": "成对记：s/z、f/v、p/b、θ/ð。",
            },
            {
                "name": "名词复数 -s 的读音",
                "rule": "复数词尾 -s 在清辅音后读 /s/，在浊辅音和元音后读 /z/，在 /tʃ/、/dʒ/、/s/ 后读 /ɪz/。",
                "examples": [
                    "books /bʊks/",
                    "bags /bæɡz/",
                    "classes /ˈklɑːsɪz/",
                ],
                "warn": "class 的复数 classes 要读 /ɪz/，不能读成 /s/ 或 /z/。",
                "tip": "s、z、ɪz 三种读法。",
            },
            {
                "name": "单词重音多在前音节",
                "rule": "双音节和多音节单词的重音一般落在第一个音节上。",
                "examples": [
                    "ˈteacher",
                    "ˈmusic",
                ],
                "warn": "重音在前音节，标音节时要把重音符号写在前面的音节前。",
                "tip": "重音往前靠。",
            },
        ],
    },
    {
        "category": "词形转换",
        "icon": "🧬",
        "level": "🟡",
        "points": [
            {
                "name": "动词变名词的常见后缀",
                "rule": "动词变名词常用 -er、-or、-ist、-tion、-ing 等后缀。",
                "examples": [
                    "teach → teacher",
                    "art → artist",
                    "decide → decision",
                ],
                "warn": "art 是美术（学科），artist 才是画家；engineering 是工程学，engineer 是工程师。",
                "tip": "先想意思，再加后缀。",
            },
            {
                "name": "名词变形容词与副词",
                "rule": "名词变形容词常用 -ful、-ous、-al、-ive 等后缀；形容词变副词一般加 -ly。",
                "examples": [
                    "use → useful",
                    "activity → active",
                    "care → careful → carefully",
                ],
                "warn": "要用形容词修饰 information，不能写 use information；care → careful 是形容词，再加 ly 才是副词。",
                "tip": "-ly 加在形容词后面变副词。",
            },
            {
                "name": "形容词变副词的拼写",
                "rule": "形容词变副词一般加 -ly；辅音字母加 y 结尾的变 -ily；-le 结尾的双写 l 再加 y。",
                "examples": [
                    "quiet → quietly",
                    "happy → happily",
                    "careful → carefully",
                ],
                "warn": "happy 变 happily，不是 happely；friendly 已经是形容词，不能再加 ly。",
                "tip": "辅音加 y：y 变 i 再加 ly。",
            },
        ],
    },
    {
        "category": "情景交际·校园生活",
        "icon": "🏫",
        "level": "🟢",
        "points": [
            {
                "name": "谈论学科与最喜欢的科目",
                "rule": "谈论学校生活时，用 What / Which + 学科名 询问科目，用 What's your favourite subject? 询问最喜欢的学科。",
                "examples": [
                    "What is your favourite subject? — It's PE.",
                    "Which subject do you like best, Maths or English?",
                    "Science is my favourite subject because it is interesting.",
                ],
                "warn": "问「最喜欢的科目是什么」要用 What，不能用 How is your favourite subject?。",
                "tip": "favourite subject 用 What 提问。",
            },
            {
                "name": "询问并谈论社团活动",
                "rule": "join a club 表示加入社团，take part in an activity 表示参加活动；介绍社团要说明时间、地点和参加对象。",
                "examples": [
                    "I want to join the AI club.",
                    "You can take part in a lot of activities after school.",
                    "The 3D printing club is from 16:00 to 17:00 on Wednesday.",
                ],
                "warn": "join 后接俱乐部，take part in 后接活动，二者不能互换，也不能漏掉 in。",
                "tip": "加入用 join，参加用 take part in。",
            },
            {
                "name": "课堂指令与指示语",
                "rule": "follow the instructions 表示遵从指令；Turn left / right. 表示转向；It's time for class. 表示该上课了；Do this eight times. 表示做这个八次。",
                "examples": [
                    "Please follow the instructions on the school noticeboard.",
                    "Turn left at the second corner and you will see the science lab.",
                    "It's time for class. Let's open our books.",
                ],
                "warn": "instruction 表示「指令」时要写成复数 instructions；祈使句的动词要用原形。",
                "tip": "祈使句发指令，动词原形开头。",
            },
            {
                "name": "作息与课程表的说法",
                "rule": "timetable 是日程表，break 指课间休息，before / after school 表示上学前和放学后。",
                "examples": [
                    "We have a 10-minute break between classes.",
                    "The film club meets every Tuesday after school.",
                    "I have seven classes every day on my timetable.",
                ],
                "warn": "课间休息说 a break between classes；after school、before school 前面都不加介词。",
                "tip": "school life 离不开 timetable 和 break。",
            },
        ],
    },
    {
        "category": "时间与频率表达",
        "icon": "🕐",
        "level": "🟢",
        "points": [
            {
                "name": "常见的五个频率副词",
                "rule": "always（总是）、usually（通常）、often（经常）、sometimes（有时）、never（从不）表示动作发生的频率。",
                "examples": [
                    "I often read English books after school.",
                    "He never goes to bed late on school nights.",
                ],
                "warn": "频率副词一般放在实义动词前、be 动词后，不能写成 He is never goes to bed late.。",
                "tip": "频率由高到低：always、usually、often、sometimes、never。",
            },
            {
                "name": "once twice 的频率表达",
                "rule": "表示频率也可用 once、twice、three times a week 这样的结构来说明多久一次。",
                "examples": [
                    "We meet three times a week to write the story.",
                    "I go swimming once a week.",
                    "The students meet twice a month.",
                ],
                "warn": "一次是 once，两次是 twice，不能写 one times a week；一周几次要在 a week 前面用 once、twice 或数字。",
                "tip": "一次 once，两次 twice。",
            },
            {
                "name": "every + 时间名词",
                "rule": "every day、every week、every Tuesday 等表示「每一」，后面直接跟名词，不加任何介词。",
                "examples": [
                    "We have English every day.",
                    "Mike goes to the movies every Friday.",
                ],
                "warn": "every 后面不加介词，不能写 every in Friday 或 in every Friday；every day 也不加 s。",
                "tip": "every 后面直接跟名词，不加介词。",
            },
            {
                "name": "时刻与时段的介词",
                "rule": "具体时刻用 at，较长的时段用 in，具体某天的上下午用 on。",
                "examples": [
                    "The club starts at 3:30 in the afternoon.",
                    "Classes begin at 8:10 on Monday.",
                    "We have a lunch break from 12:00 to 1:00.",
                ],
                "warn": "in the afternoon 用 in，但 on Monday afternoon 用 on，两个不能混。",
                "tip": "at 点，in 大段时间，on 具体某天。",
            },
        ],
    },
    {
        "category": "句子成分与基本句型",
        "icon": "🧮",
        "level": "🟢",
        "points": [
            {
                "name": "句子的主语和谓语",
                "rule": "每个句子都必须有主语和谓语；主语说明「谁」，谓语说明「做什么」。",
                "examples": [
                    "The students / are singing / a song.",
                    "My mother / gets up / early every day.",
                ],
                "warn": "缺主语或缺谓语的句子不成立，不能写 The students singing a song.。",
                "tip": "先找主语，再找谓语。",
            },
            {
                "name": "宾语是动作的对象",
                "rule": "宾语说明动作的承受者，一般放在及物动词后面。",
                "examples": [
                    "We do our homework in the classroom.",
                    "He plays the guitar on Sundays.",
                ],
                "warn": "homework 是不可数名词，不能加 a，不能写 do a homework.。",
                "tip": "动词后面接动作的对象。",
            },
            {
                "name": "表语说明主语是什么",
                "rule": "be 动词后面的成分叫表语，说明主语是什么或怎么样。",
                "examples": [
                    "My favourite subject is PE.",
                    "The film club is open to Grade 6 students.",
                    "Miss Lin is tall and friendly.",
                ],
                "warn": "be 动词后面不能直接跟动词原形，不能写 The club is join the film club.。",
                "tip": "be 后面就是表语。",
            },
            {
                "name": "状语说明时间地点方式",
                "rule": "状语说明动作发生的时间、地点或方式，常常用介词短语表示。",
                "examples": [
                    "We have classes at 8:00.",
                    "She speaks English very well.",
                    "The film club meets on Tuesday.",
                ],
                "warn": "状语中的介词搭配不能错，speak in English 对，speak with English 错。",
                "tip": "时间、地点、方式都是状语。",
            },
        ],
    },
    {
        "category": "高频易错点汇总",
        "icon": "⚠️",
        "level": "🟡",
        "points": [
            {
                "name": "there be 就近原则易错",
                "rule": "there be 的 be 动词跟着离它最近的那个名词走，和前面的主语无关。",
                "examples": [
                    "There is a computer and two chairs in the lab.",
                    "There are two English books and a pencil on the desk.",
                ],
                "warn": "看的是紧跟在 be 后面的名词：There is a computer and two chairs. 前面有 a computer，所以用 is。",
                "tip": "就近原则，就近看名词。",
            },
            {
                "name": "与……不同用 from",
                "rule": "be different from 表示「与……不同」，介词固定用 from。",
                "examples": [
                    "My bedroom is different from my twin sister's.",
                    "How is Lisa's timetable different from Mike's?",
                ],
                "warn": "不能写 different to 或 different with，正确搭配只有 be different from。",
                "tip": "different 后面只跟 from。",
            },
            {
                "name": "be similar to 的搭配",
                "rule": "be similar to 表示「与……相似」，介词用 to；它和 be different from 正好相反。",
                "examples": [
                    "Look! Your schoolbag is similar to Lily's.",
                    "My timetable is similar to Jack's.",
                ],
                "warn": "不能写 be similar from，similar 后面必须接 to。",
                "tip": "different 配 from，similar 配 to。",
            },
            {
                "name": "可数用 many 不可数用 much",
                "rule": "提问可数名词的数量用 how many，提问不可数名词的数量或价钱用 how much。",
                "examples": [
                    "How many clubs do you have on your timetable?",
                    "How much water is there in the bottle?",
                ],
                "warn": "不能说 How many water is there in the bottle?；也不要说 How much clubs。",
                "tip": "可数 many，不可数 much。",
            },
            {
                "name": "频率与时长提问辨析",
                "rule": "how often 提问频率，how long 提问时间长度。",
                "examples": [
                    "How often do you take part in the club activities? — Twice a week.",
                    "How long do you have a break between classes? — Ten minutes.",
                ],
                "warn": "问「多久一次」不能用 how long，问「多长时间」也不能用 how often。",
                "tip": "often 问频率，long 问时长。",
            },
            {
                "name": "every 后面不加介词",
                "rule": "every + 时间名词表示「每一」，后面直接跟名词，前面不加任何介词。",
                "examples": [
                    "We have English every day.",
                    "Mike goes to the movies every Friday.",
                ],
                "warn": "不能写 in every day 或 every in Friday，正确写法是 every day、every Friday。",
                "tip": "every 后面直接跟名词。",
            },
            {
                "name": "a lot of 后用复数名词",
                "rule": "a lot of 后面接可数名词的复数形式，和 lots of 用法相同。",
                "examples": [
                    "You can take part in a lot of activities after school.",
                    "We did a lot of experiments in the science lab.",
                ],
                "warn": "activity 是可数名词，不能说 a lot of activity，要用 a lot of activities；a lot of 和 lots of 意思一样。",
                "tip": "a lot of = lots of，后面可数名词用复数。",
            },
            {
                "name": "白天用 in 夜里用 at",
                "rule": "上午、下午、傍晚用 in the morning / afternoon / evening；夜里用 at night。",
                "examples": [
                    "We have four classes in the morning.",
                    "I read English books at night.",
                ],
                "warn": "不能说 in the night，也不能说 at the morning；具体时刻才用 at，如 at 8:00 in the morning。",
                "tip": "白天 in，夜里 at。",
            },
            {
                "name": "迟到某事用 be late for",
                "rule": "be late for + 场合表示「迟到、赶不上」；be late 单独用表示「晚了、迟了」。",
                "examples": [
                    "Don't be late for the first class.",
                    "Sorry, I'm late.",
                ],
                "warn": "迟到某项活动用 be late for，不能说 be late to class；单独说晚了才用 be late。",
                "tip": "迟到某事用 for，单独说晚了用 be late。",
            },
            {
                "name": "该做某事有两种说法",
                "rule": "It's time for + 名词，表示「到了……的时间」；It's time to do sth. 表示「该做某事了」。",
                "examples": [
                    "It's time for class.",
                    "It's time to open our books.",
                    "It's time for lunch.",
                ],
                "warn": "It's time for 后面跟名词，不能跟动词原形；It's time to do 后面才跟动词原形。",
                "tip": "for 接名词，to 接动词原形。",
            },
        ],
    },
]
