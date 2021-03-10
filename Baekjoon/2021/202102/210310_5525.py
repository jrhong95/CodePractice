import sys
read = sys.stdin.readline

N = int(read())
_ = read()
S = read().rstrip()
P = "I" + "OI" * N


def get_pi(s):
    pi = [0] * len(P)
    j = 0

    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if P[i] == P[j]:
            j += 1
            pi[i] = j

    return pi


def kmp(src, pat):
    pi = get_pi(pat)
    j = 0

    answer = 0
    for i, c in enumerate(src):
        while j > 0 and c != pat[j]:
            j = pi[j - 1]

        if src[i] == pat[j]:
            if j == len(pat) - 1:
                answer += 1
                j = pi[j]
            else:
                j += 1
    return answer


if __name__ == "__main__":
    print(kmp(S, P))
