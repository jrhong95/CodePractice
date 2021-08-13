import sys
from copy import deepcopy
from itertools import permutations

read = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
R, C, K = map(int, read().split())
A = [list(map(int, read().split())) for _ in range(R)]
commands = [tuple(map(int, read().split())) for _ in range(K)]


def get_min_sum(A):
    return min(list(sum(line) for line in A))


def rotate(A, center_r, center_c, s):
    start_r, start_c = center_r - s - 1, center_c - s - 1
    end_r, end_c = center_r + s - 1, center_c + s - 1

    while start_r != end_r and start_c != end_c:
        cur_r, cur_c = start_r, start_c
        before = A[start_r][start_c]

        for i in range(4):
            next_r, next_c = cur_r, cur_c

            while start_r <= next_r <= end_r and start_c <= next_c <= end_c:
                next_r += dr[i]
                next_c += dc[i]

                if not start_r <= next_r <= end_r or not start_c <= next_c <= end_c:
                    break

                tmp = A[next_r][next_c]
                A[next_r][next_c] = before
                before = tmp

                cur_r, cur_c = next_r, next_c

        start_r += 1
        start_c += 1
        end_r -= 1
        end_c -= 1


def main():
    ans = sys.maxsize
    for command in permutations(commands):
        new_a = deepcopy(A)
        for r, c, s in command:
            rotate(new_a, r, c, s)
        ans = min(get_min_sum(new_a), ans)
    print(ans)


main()