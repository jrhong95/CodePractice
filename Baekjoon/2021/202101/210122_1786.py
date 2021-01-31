import sys
read = sys.stdin.readline


def make_pi(find):
    pi = [0] * len(find)
    j = 0

    for i in range(1, len(find)):
        while j > 0 and find[i] != find[j]:
            j = pi[j - 1]

        if find[i] == find[j]:
            j += 1
            pi[i] = j

    return pi


def kmp_find(src, pattern):
    pi = make_pi(pattern)
    j = 0

    answer = []
    for i, c in enumerate(src):
        while j > 0 and c != pattern[j]:
            j = pi[j - 1]

        if src[i] == pattern[j]:

            if j == len(pattern) - 1:
                answer.append(i - j + 1)
                j = pi[j]
            else:
                j += 1

    return answer


txt = read().rstrip()
find = read().rstrip()
answer = kmp_find(txt, find)

print(len(answer))
print(*answer, sep='\n')
