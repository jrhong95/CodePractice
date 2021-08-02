CUTE = "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"
NO_CUTE = "흥칫뿡!! <(￣ ﹌ ￣)>"

S = list(map(int, list(input())))
if len(S) == 1:
    print(CUTE)
else:
    diff = S[0] - S[1]
    for i in range(len(S) - 1):
        if S[i] - S[i + 1] != diff:
            print(NO_CUTE)
            break
    else:
        print(CUTE)
