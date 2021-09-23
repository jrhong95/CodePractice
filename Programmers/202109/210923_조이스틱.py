def solution(name):
    move = [min(ord(n) - ord("A"), ord("Z") - ord(n) + 1) for n in name]
    idx, answer = 0, 0

    while True:
        answer += move[idx]
        move[idx] = 0
        for m in move:
            if m:
                break
        else:
            return answer

        for i in range(len(name)):
            left = idx - i
            right = idx + i
            if move[right]:
                idx = right
                break
            if move[left]:
                idx = left
                break

        answer += i