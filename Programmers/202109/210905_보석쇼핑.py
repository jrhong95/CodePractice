def solution(gems):
    gem_dict = {gem: 0 for gem in gems}
    goal_count, gem_count = len(gem_dict), 0

    left, right = 0, 0
    min_left, min_right, min_len = 0, 0, 10 ** 9

    while right <= len(gems):
        if gem_count < goal_count:
            if right == len(gems):
                break

            if gem_dict[gems[right]] == 0:
                gem_count += 1
            gem_dict[gems[right]] += 1
            right += 1

        else:
            gem_sum = sum(gem_dict.values())
            if min_len > gem_sum:
                min_left, min_right, min_len = left, right, gem_sum

            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                gem_count -= 1
            left += 1

    return [min_left + 1, min_right]