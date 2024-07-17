# a dict of keys to exclude from adding to the glossary.
# please include a reason as to why we're ignoring a string.
# ex: "こ": "Not a DQX term."

IGNORE = {
    "": "Blank string. We don't want to use this.",
    "・": "Not a DQX term.",
    "こ": "Not a DQX term.",
    "-": "Not a DQX term.",
    ",": "Not a DQX term.",
    "Ａ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "Ｋ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "Ｑ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "Ｊ": "Not a DQX term. Single letter coming through after glossary sanitize.",
    "！": "Don't replace punctuation.",
    "？": "Don't replace punctuation.",
    "無効": "'Null' in Weblate.",
    "あ": "The letter A. We don't want to replace this.",
    "現": "'P.' in Weblate.",
    "草": "'Grass' in Weblate.",
    "仮": "'Temporary' string in Weblate.",
    "真": "'T.' in Weblate.",
    "偽": "'F.' in Weblate.",
    "階": "'F.' in Weblate.",
    "西": "'West' in Weblate.",
    "南": "'South' in Weblate.",
    "北": "'North' in Weblate.",
    "東": "'East' in Weblate.",
    "犬": "'Dog' in Weblate.",
    "主": "'Lord' in Weblate.",
    "月": "'Mn.' in Weblate.",
    "扉": "'Door' in Weblate.",
    "筒": "'Tube' in Weblate.",
    "迷惑料を払いやがれ！": "Quest phrase that appears in dialogue",
    "闘志": "Quest phrase that appears in dialogue",
    "真の敵は": "Quest phrase that appears in dialogue",
    "やさしさに包まれて": "Quest phrase that appears in dialogue",
    "遠い約束": "Quest phrase that appears in dialogue",
    "鶏": "CKN in Weblate",
    "タコ": "OCT in Weblate",
    "歌姫": "DVA in Weblate",
    "閃光": "SPA in Weblate",
    "竜化": "DGN in Weblate",
    "うさ": "RAB in Weblate",
    "魔剣": "DMN in Weblate",
    "ジャ": "JAK in Weblate",
    "詩人": "POE in Weblate",
    "真の": "T. in Weblate",
    "橋": "Capatalized 'Bridge' in Weblate",
    "てて": "Tete in Weblate, common string of characters",
    "天使": "ANG in Weblate",
    "タイ": "Red Snapper in Weblate, common string of characters",
    "掘る": "'Dig' in Weblate, regular word",
    "下階": "'Down' in Weblate, regular word",
    "ネコ": "'Cat' in Weblate, regular word",
    "民家": "'House' in Weblate, regular word",
    "セス": "Player name Seth, common string of characters",
    "全て": "'All' in Weblate, common word",
    "わか": "'KLP' in Weblate, common string of characters",
    "上階": "Up in Weblate, regular word",
    "泣く": "Cry in Weblate, regular word",
    "１階": "1F in Weblate, don't want abbreviated",
    "２階": "2F in Weblate, don't want abbreviated",
    "３階": "3F in Weblate, don't want abbreviated",
    "４階": "4F in Weblate, don't want abbreviated",
    "５階": "5F in Weblate, don't want abbreviated",
    "６階": "6F in Weblate, don't want abbreviated",
    "７階": "7F in Weblate, don't want abbreviated",
    "８階": "8F in Weblate, don't want abbreviated",
    "９階": "9F in Weblate, don't want abbreviated",
    "くさ": "Grass? in Weblate, common string of characters",
    "魔使": "MGE in Weblate, don't want abbreviated",
    "地下１階": "B1F in Weblate, don't want abbreviated",
    "地下２階": "B2F in Weblate, don't want abbreviated",
    "地下３階": "B3F in Weblate, don't want abbreviated",
    "地下４階": "B4F in Weblate, don't want abbreviated",
    "地下５階": "B5F in Weblate, don't want abbreviated",
    "地下６階": "B6F in Weblate, don't want abbreviated",
    "地下７階": "B7F in Weblate, don't want abbreviated",
    "地下８階": "B8F in Weblate, don't want abbreviated",
    "地下９階": "B9F in Weblate, don't want abbreviated",
    "王子": "PRC in Weblate, don't want abbreviated",
    "なし": "None in Weblate, common word",
    "詩人": "POE in Weblate, don't want abbreviated",
    "欠番": "Miss# in Weblate, can just ignore",
    "辛党": "SPI in Weblate, don't want abbreviated",
    "出口": "Exit in Weblate, normal word",
    "入口": "Entrance in Weblate, normal word",
    "デス": "DTH in Weblate, common string",
    "武闘": "MRT in Weblate, don't want abbreviated",
    "レン": "RNG in Weblate, don't want abbreviated",
    "ぶた": "PIG in Weblate, don't want capitalized",
    "の間": "Chamber in Weblate, common word",
    "怪盗": "THF in Weblate, don't want abbreviated",
    "あく": "DEM in Weblate, don't want abbreviated",
    "ねじ": "Screw in Weblate, too short/common word",
    "外観": "Exterior in Weblate, common word",
    "戦士": "WAR in Weblate, don't want abbreviated",
    "甘党": "SWT in Weblate, don't want abbreviated",
    "地下": "Underground in Weblate, common word",
    "オバ": "GHO in Weblate, don't want abbreviated",
    "王女": "PRN in Weblate, don't want abbreviated",
    "廊下": "Corridor in Weblate, common word",
    "彼女": "Her in Weblate, too common a word",
    "闘士": "WAR in Weblate, don't want abbreviated",
    "怒る": "Angry in Weblate, too common a word",
    "勇者": "HRO in Weblate, don't want abbreviated",
    "くら": "MAN in Weblate, too short a string",
    "逃走": "ESC in Weblate, don't want abbreviated",
    "ミス": "Miss in Weblate, too short a string",
    "ミイ": "MUM in Weblate, too short a string",
    "マリ": "SEA in Weblate, too short a string",
    "ラン": "LMP in Weblate, too short a string",
    "時監": "TME in Weblate, don't want abbreviated",
    "震天": "HSK in Weblate, don't want abbreviated",
    "守護": "protection in Weblate, too short a string",
    "真偽": "True or False in Weblate, too short a phrase",
    "剣士": "SWD in Weblate, don't want abbreviated",
    "竜術": "DGM in Weblate, don't want abbreviated",
    "パン": "PMK in Weblate, too short a word",
    "しち": "Value in Weblate, too short a string",
    "かべ": "Wall in Weblate, too short a string",
    "ねこ": "Cat in Weblate, normal word",
    "狩人": "HNT in Weblate, don't want abbreviated",
    "地下": "Below in Weblate, normal word",
    "だい": "SQD in Weblate, too short a string",
    "スタ": "STR in Weblate, too short a string",
    "はし": "Bridge in Weblate, too short a string",
    "賢哲": "WIS in Weblate, don't want abbreviated",
    "下り": "Down in Weblate, common word",
    "ドラ": "DRA in Weblate, too short of a string",
    "オン": "On in Weblate, too short of a string",
    "闘志": "The Will to Fight in Weblate, don't want word to use quest phrase",
    "新品": "New in Weblate, a common word",
    "天地": "DRU in Weblate, don't want abbreviated",
    "僧侶": "PRI in Weblate, don't want abbreviated",
    "追跡": "TRA in Weblate, don't want abbreviated",
    "パラ": "PLD in Weblate, don't want abbreviated",
    "の丘陵": "Hills of Weblate, fragment of a phrase that would look weird",
    " 出口": "Exit in Weblate, normal word (space is intentional)",
    "もち": "Mochi in Weblate, too short a string",
    "パー": "Paper in Weblate, too short a string",
    "グー": "Rock in Weblate, too short a string",
    "やり": "Spear in Weblate, too short a string",
    "あると": "Alto in Weblate, too common",
    "うら": "Tails in Weblate, too short a string",
    "ごめんなさい": "Decline in Weblate, this is not the correct definition",
    "お願い": "Please! in Weblate, too common a phrase",
    "アジ" : "Horse Mackerel in Weblate, too short a string",
    "いただきます": "Let's eat in Weblate, not always used this way",
    "みろ": "Miro in Weblate, too short a string",
    "ミロ": "Miro in Weblate, too short a string"
}
