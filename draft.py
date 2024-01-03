import random

verbs_list = [
    ("be", "was/were"),
    ("become", "became"),
    ("begin", "began"),
    ("blow", "blew"),
    ("break", "broke"),
    ("bring", "brought"),
    ("build", "built"),
    ("buy", "bought"),
    ("can", "could"),
    ("catch", "caught"),
    ("choose", "chose"),
    ("come", "came"),
    ("cost", "cost"),
    ("cut", "cut"),
    ("do", "did"),
    ("draw", "drew"),
    ("drink", "drank"),
    ("drive", "drove"),
    ("eat", "ate"),
    ("fall", "fell"),
    ("feed", "fed"),
    ("feel", "felt"),
    ("find", "found"),
    ("fly", "flew"),
    ("forget", "forgot"),
    ("get", "got"),
    ("give", "gave"),
    ("go", "went"),
    ("grow", "grew"),
    ("have", "had"),
    ("hear", "heard"),
    ("hit", "hit"),
    ("hold", "held"),
    ("keep", "kept"),
    ("know", "knew"),
    ("learn", "learnt"),
    ("leave", "left"),
    ("let", "let"),
    ("lose", "lost"),
    ("make", "made"),
    ("meet", "met"),
    ("pay", "paid"),
    ("read", "read"),
    ("ring", "rang"),
    ("run", "ran"),
    ("say", "said"),
    ("see", "saw"),
    ("sell", "sold"),
    ("send", "sent"),
    ("sing", "sang"),
    ("sit", "sat"),
    ("sleep", "slept"),
    ("speak", "spoke"),
    ("spend", "spent"),
    ("stand", "stood"),
    ("swim", "swam"),
    ("take", "took"),
    ("teach", "taught"),
    ("tell", "told"),
    ("think", "thought"),
    ("throw", "threw"),
    ("understand", "understood"),
    ("wake", "woke"),
    ("wear", "wore"),
    ("win", "won"),
    ("write", "wrote"),
    ("beat", "beat"),
    ("bend", "bent"),
    ("bet", "bet"),
    ("bite", "bit"),
    ("bleed", "bled"),
    ("burn", "burnt"),
    ("dig", "dug"),
    ("hang", "hung"),
    ("lend", "lent"),
    ("lie", "lay"),
    ("put", "put"),
    ("ride", "rode"),
    ("set", "set"),
    ("shake", "shook"),
    ("shoot", "shot"),
    ("show", "showed"),
    ("sink", "sank"),
    ("spell", "spelt"),
    ("split", "split"),
    ("spread", "spread"),
    ("steal", "stole"),
    ("strike", "struck")
]


random.seed(42)
print("test number", ":")
random.shuffle(verbs_list)

next_text = []
good = [0,2,3,5,6,10,11,12,15,18,19,24,26,29,32,34,36,38,39,41,43,44,48,49,51,57,59,62,63,68,70,71,72,73,75,78,80,81,83,86]
for i in range(len(verbs_list)):
    if i not in good:
        next_text.append(verbs_list[i])
        # print(i,") ",verbs_list[i][0],"- ")
    # print(i,") ",verbs_list[i])

# for i in range(len(verbs_list)):
#     print("ans to test number", iter, ":")
#     # print(i,") ",verbs_list[i][0],"- ")
#     print(i,") ",verbs_list[i])








verbs_list = next_text
random.seed(78)
for iter1 in range(3):
    print("test number",iter1+1,":")
    random.shuffle(verbs_list)
    for i in range(0, len(verbs_list), 4):
        line = f"{i + 1}) {verbs_list[i][0]} -                          | "
        if i + 1 < len(verbs_list):
            line += f"{i + 2}) {verbs_list[i + 1][0]} -                          | "
        if i + 2 < len(verbs_list):
            line += f"{i + 3}) {verbs_list[i + 2][0]} -                          | "
        if i + 3 < len(verbs_list):
            line += f"{i + 4}) {verbs_list[i + 3][0]} -                            "
        print(line)

#         # print(i,") ",verbs_list[i])

    # for i in range(len(verbs_list)):
    #     print("ans to test number", iter, ":")
    #     # print(i,") ",verbs_list[i][0],"- ")
    #     print(i,") ",verbs_list[i])
    #


