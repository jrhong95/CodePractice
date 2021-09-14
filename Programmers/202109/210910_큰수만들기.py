def solution(number, k):
    big, cnt = [], k
    for n in number:
        while big and big[-1] < n and cnt > 0:
            big.pop()
            cnt -= 1
        big.append(n)
    return "".join(big[: len(number) - k])
