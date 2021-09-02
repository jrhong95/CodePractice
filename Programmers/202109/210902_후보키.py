from itertools import combinations


def is_minimal(cand_list, target):
    for num in cand_list:
        common_num = target & num
        if common_num and common_num == num:
            return False
    return True


def solution(relation):
    r_len, c_len = len(relation), len(relation[0])
    candidate_mask = []

    for i in range(1, c_len + 1):
        for comb in combinations(range(c_len), i):
            tmp_candidate_key = [[rel[n] for rel in relation] for n in comb]

            if len(set(zip(*tmp_candidate_key))) == r_len:
                cur_cand_num = sum(2 ** n for n in comb)
                if is_minimal(candidate_mask, cur_cand_num):
                    candidate_mask.append(cur_cand_num)

    return len(candidate_mask)