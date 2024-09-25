grammarArray = [
	{
		"grammarForm": "Noun-에",
		"regex": "ㅇㅔ(?!ㅅㅓ)",
		"description": "Particle -에. Time or place. DO NOT USE FOR -에서",
		"patternMatch": "-에\s+",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-2/#new"
	},
	{
		"grammarForm": "-은/는 (Topic Particle)",
		"regex": "ㅇㅡㄴ\s+|ㄴㅡㄴ\s+",
		"description": "Topic Particle -은/는.",
		"patternMatch": "-은\s+|-는\s+",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-1/#kp"
	},
	{
		"grammarForm": "-을/를 (Object Particle)",
		"regex": "ㅇㅡㄹ\s+|ㄹㅡㄹ\s+",
		"description": "Object Particle -을/를.",
		"patternMatch": "-을\s+|-를\s+",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-1/#kp"
	},
	{
		"grammarForm": "-이/가 (Subject Particle)",
		"regex": "ㅇㅣ\s+|ㄱㅏ\s+",
		"description": "Subject Particle -이/가.",
		"patternMatch": "-이\s+|-가\s+",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-2/#203"
	},
	{
		"grammarForm": "Adjective + -ㄴ/은",
		"regex": "[ㅓㅕㅐㅙㅞㅔㅝㅚㅟㅣㅏㅑㅗㅛㅜㅠㅡ]ㄴ\s+",
		"description": "Adjective forming suffix. Adjective + -ㄴ/은",
		"patternMatch": "-ㄴ\s+",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-4/"
	},
	{
		"grammarForm": "Noun-도",
		"regex": "ㄷㅗ",
		"description": "Particle -도. To, as well, also, etc.",
		"patternMatch": "-도\s+",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-4/#do"
	},
	{
		"grammarForm": "Verb-ㄴ/는다",
		"regex": "[ㅣㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ]ㄴㄷㅏ",
		"description": "Plain form present tense for verbs",
		"patternMatch": "~ㄴ다\s*|-는다\s*",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/#vpres"
	},
	{
		"grammarForm": "-었/았다 (Past tense)",
		"regex": "[ㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ]ㅆ",
		"description": "Past tense for verbs",
		"patternMatch": "~었-|~았-",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/#vpast"
	},
	{
		"grammarForm": "-겠다 (Future tense)",
		"regex": "[ㄱㅔㅆ][가-힣]+",
		"description": "Future tense for verbs",
		"patternMatch": "-겠다",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/#vfut"
	},
	{
		"grammarForm": "-다 (Plain form)",
		"regex": "[다]",
		"description": "Plain form present tense for adjectives",
		"patternMatch": "-다\s*",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/#apres"
	},
	{
		"grammarForm": "-었/았다 (Past tense)",
		"regex": "[ㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ][ㅆ][가-힣]+",
		"description": "Past tense for adjectives",
		"patternMatch": "-었-|-았-",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/#apast"
	},
	{
		"grammarForm": "-겠다 (Future tense)",
		"regex": "[ㄱㅔㅆ][가-힣]+",
		"description": "Future tense for adjectives",
		"patternMatch": "-겠다",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/#afut"
	},
	{
		"grammarForm": "-어요/아요 (Informal honorific ending)",
		"regex": "ㅇㅛ",
		"description": "Informal respectful sentence ending",
		"patternMatch": "-어요\s*|-아요\s*",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-6/#verbandpres"
	},
	{
		"grammarForm": "-ㅂ니다/습니다 (Honorific ending)",
		"regex": "[ㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ]ㅂㄴㅣㄷㅏ|ㅅㅡㅂㄴㅣㄷㅏ",
		"description": "Formal sentence ending",
		"patternMatch": "-ㅂ니다\s*|-습니다\s*",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-6/#verbandpres"
	},
	{
		"grammarForm": "-(이)야 (Informal ending)",
		"regex": "[ㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ]ㅇㅑ|ㅇㅣㅇㅑ",
		"description": "Informal setence ending for 이다",
		"patternMatch": "-이야\s*|~야\s*",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/unit-1-lesson-9/#conj"
	},
	
	{
		"grammarForm": "-이에요/예요 (Informal honorific ending)",
		"regex": "[ㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ]ㅇㅖㅇㅛ|ㅇㅣㅇㅔㅇㅛ",
		"description": "Informal respectful setence ending for 이다",
		"patternMatch": "-이에요|~예요",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/unit-1-lesson-9/#conj"
	},
	{
		"grammarForm": "-입니다 (Honorofic ending)",
		"regex": "ㅇㅣㅂㄴㅣㄷㅏ",
		"description": "Formal setence ending for 이다",
		"patternMatch": "-입니다\s*",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/unit-1-lesson-9/#conj"
	},
	{
		"grammarForm": "-ㄹ/을 것이다 (Future tense)",
		"regex": "ㄹ\s*ㄱㅓㅅㅇㅣㄷㅏ",
		"description": "Future tense sentence ending",
		"patternMatch": "-ㄹ 것-|-ㄹ 거-",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/unit-1-lesson-9/#conj"
	},
	{
		"grammarForm": "Noun-적(이다)",
	    "regex": "ㅈㅓㄱ(?:ㅇㅣ)",
        "description": "Suffix to change noun into descriptive word",
		"patternMatch": "-적",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-16/"
	},
	{
		"grammarForm": "Noun-스럽다",
	    "regex": "ㅅㅡㄹㅓㅂㄷㅏ|ㅅㅡㄹㅓㅇㅜ",
        "description": "Suffix/sentence ending to change noun into descriptive word",
		"patternMatch": "-스럽다 | -스러우-",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-16/"
	},
	{
		"grammarForm": "Noun-들 (Plural)",
	    "regex": "ㄷㅡㄹ",
        "description": "Particle added to nouns to make them plural",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-12/#kp1"
	},
    {
		"grammarForm": 'Noun-만 ("Only")',
	    "regex": "ㅁㅏㄴ",
        "description": "Particle added to nouns to mean only",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-12/#kp2"
	},
    {
		"grammarForm": 'Noun-에서',
	    "regex": "ㅇㅔㅅㅓ",
        "description": "Particle added to show location where something occurs",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-12/#kp3"
	},
    {
		"grammarForm": 'Noun-부터',
	    "regex": "ㅂㅜㅌㅓ",
        "description": "Particle added to show place or time something starts or begins",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-12/#kp4"
	},
    {
		"grammarForm": 'Noun-까지',
	    "regex": "ㄲㅏㅈㅣ",
        "description": "Particle added to show place or time something ends",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-12/#kp4"
	},
    {
		"grammarForm": 'Noun-(으)로',
	    "regex": "(?:ㅇㅡ)ㄹㅗ+",
        "description": "Particle added to show direction, method, how something is done, or a choice",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/lesson-12/#kp5"
	},
    {
		"grammarForm": '-고 (Clausal connecting)',
	    "regex": "ㄱㅗ",
        "description": "Attached to action or descriptive verb to connect two clauses",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-17/#co"
	},
    {
		"grammarForm": '-아/어서 (Clausal connecting)',
	    "regex": "[ㅏㅓㅑㅕㅐㅔㅝㅘㅖㅒㅞ]ㅅㅓ",
        "description": "Attached to action or descriptive verb to connect two clauses",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-17/#co3"
	},
    {
		"grammarForm": '-고 싶다',
	    "regex": "ㄱㅗ\s*ㅅㅣㅍ",
        "description": "Shows that one wants to do something. Attached to verbs.",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-17/#co4"
	},
    {
		"grammarForm": '-고 있다 (Progressive tense)',
	    "regex": "ㄱㅗ\s*ㅇㅣㅆ",
        "description": "Attached to verb to make progressive tense",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-18/#ppt"
	},
    {
		"grammarForm": '-아/어지다',
	    "regex": "[ㅏㅓㅑㅕㅐㅔㅝㅘㅖㅒㅞ]ㅈ[ㅣㅕ]",
        "description": "Attached to descriptive verb to mean that something becomes that adjective",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-18/#a"
	},
    {
		"grammarForm": 'Noun-보다 (Comparison)',
	    "regex": "ㅂㅗㄷㅏ",
        "description": "Attached to a noun to compare something to the noun",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-19/#compa3"
	},
    {
		"grammarForm": '-ㅂ/습니까 (Question ending)',
	    "regex": "[ㅏㅓㅡㅜㅗㅑㅕㅠㅛㅐㅔㅟㅝㅚㅘㅢㅖㅒㅞ]ㅂㄴㅣㄲㅏ|ㅅㅡㅂㄴㅣㄲㅏ",
        "description": "Formal sentence ending for a question",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-21-asking-questions-in-korean-why-when-where-and-who/#212"
	},
    {
		"grammarForm": '-니 (Question ending)',
	    "regex": "ㄴㅣ",
        "description": "Informal sentence ending for a question",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-21-asking-questions-in-korean-why-when-where-and-who/#213"
	},
    {
		"grammarForm": '-ㄴ/은가(요) (Question ending)',
	    "regex": "ㄴㄱㅏ",
        "description": "Sentence ending to help soften a question",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-21-asking-questions-in-korean-why-when-where-and-who/#213"
	},
    {
		"grammarForm": '-나(요) (Question ending)',
	    "regex": "ㄴㅏ",
        "description": "Sentence ending to help soften a question",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-21-asking-questions-in-korean-why-when-where-and-who/#21new"
	},
    {
		"grammarForm": '의 (Possessive Particle)',
	    "regex": "ㅇㅢ|ㅇㅡㅣ",
        "description": "Particle attached to noun to make possessive",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-3/#%EC%9D%98"
	},
    {
		"grammarForm": '전 (Before)',
	    "regex": "ㅈㅓㄴ",
        "description": "Used to mean before or some period of time ago",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-24/#242"
	},
    {
		"grammarForm": '후 (After)',
	    "regex": "ㅎㅜ",
        "description": "Used to mean after or some period of time from now",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-24/#243"
	},
    {
		"grammarForm": '-마다 (Each, Every)',
	    "regex": "ㅁㅏㄷㅏ",
        "description": "Attached to noun to mean each or every",
		"link": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/lesson-25/#255"
	},

]