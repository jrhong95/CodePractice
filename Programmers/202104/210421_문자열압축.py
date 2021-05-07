def solution(s):
    answer = []
    if len(s) <= 1:
        return 1
    for length in range(1, len(s) // 2 + 1):
        words = [s[i: i + length] for i in range(0, len(s), length)]

        tmp, cnt, compress = "", 1, ""
        for i, word in enumerate(words):
            if tmp == "":
                tmp = word
            else:
                if word == tmp:
                    cnt += 1
                else:
                    compress += tmp if cnt == 1 else str(cnt) + tmp
                    cnt = 1
                    tmp = word

        compress += tmp if cnt == 1 else str(cnt) + tmp
        answer.append(len(compress))

    return min(answer)


print(solution("a"))
# solution("xababcdcdababcdcd")
