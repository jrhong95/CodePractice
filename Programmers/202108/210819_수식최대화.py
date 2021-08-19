import re
from itertools import permutations


def solution(expression):
    numbers = list(map(int, re.split("[*+-]", expression)))
    ops = [i for i in expression if not i.isdigit()]
    set_ops = set(ops)

    answer = 0
    for cand in permutations(set_ops, len(set_ops)):
        cur_numbers = numbers[:]
        cur_ops = ops[:]

        for c_op in cand:
            idx = 0
            while idx < len(cur_ops):
                if cur_ops[idx] == c_op:
                    if c_op == "-":
                        cur_numbers[idx] -= cur_numbers[idx + 1]
                    elif c_op == "+":
                        cur_numbers[idx] += cur_numbers[idx + 1]
                    else:
                        cur_numbers[idx] *= cur_numbers[idx + 1]
                    cur_numbers.pop(idx + 1)
                    cur_ops.pop(idx)
                else:
                    idx += 1
        answer = max(answer, abs(cur_numbers[0]))

    return answer