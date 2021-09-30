import sys

read = sys.stdin.readline

roma_to_int = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}
int_to_roma = {n: c for c, n in roma_to_int.items()}
n1 = read().rstrip()
n2 = read().rstrip()


def to_int(roma):
    i = 0
    ret = 0
    while i < len(roma):
        if i + 1 < len(roma) and roma[i : i + 2] in roma_to_int:
            ret += roma_to_int[roma[i : i + 2]]
            i += 2
        else:
            ret += roma_to_int[roma[i]]
            i += 1
    return ret


def main():
    num = to_int(n1) + to_int(n2)
    ret = ""
    print(num)
    while num > 0:
        for n in int_to_roma.keys().__reversed__():
            cnt, num = divmod(num, n)
            ret += int_to_roma[n] * cnt

    print(ret)


main()
