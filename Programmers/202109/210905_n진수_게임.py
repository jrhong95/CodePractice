not_list = "0123456789ABCDEF"


def make_n_notation(num, n):
    ret = []
    while num >= n:
        ret.append(not_list[num % n])
        num //= n
    return not_list[num] + "".join(ret[::-1])


def solution(n, t, m, p):
    nums = "".join([make_n_notation(i, n) for i in range(t * m + 1)])
    return "".join(nums[p - 1 + m * i] for i in range(t))