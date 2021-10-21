def make_3_notation(n):
    if n < 3:
        return str(n)
    n, m = divmod(n, 3)
    return str(make_3_notation(n)) + str(m)


def notation_to_number(notation):
    return sum(int(c) * (3 ** i) for i, c in enumerate(notation))


def solution(n):
    return notation_to_number(make_3_notation(n))