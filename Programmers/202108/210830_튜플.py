def solution(s):
    ans = []
    tmp_num, tmp_tuple, tmp_list = "", [], []
    is_digit = False

    for c in s[1:-1]:
        if c == "{":
            tmp_tuple = []
        elif c.isdigit():
            tmp_num += c
            is_digit = True
        elif c == "," and is_digit:
            tmp_tuple.append(int(tmp_num))
            tmp_num = ""
            is_digit = False
        elif c == "}":
            tmp_tuple.append(int(tmp_num))
            is_digit = False
            tmp_num = ""
            tmp_list.append(tmp_tuple)

    for l in sorted(tmp_list, key=lambda x: len(x)):
        ans.extend(l)

    return list(dict.fromkeys(ans))