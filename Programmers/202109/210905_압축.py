def solution(msg):
    last_idx = 27
    dic = {chr(ord("A") + i - 1): i for i in range(1, last_idx)}
    answer = []
    idx, tmp_word = 0, msg[0]

    while True:
        if tmp_word in dic:
            idx += 1
            if idx == len(msg):
                break
            tmp_word += msg[idx]
        else:
            dic[tmp_word] = last_idx
            last_idx += 1
            answer.append(dic[tmp_word[:-1]])
            tmp_word = msg[idx]
    answer.append(dic[tmp_word])
    return answer