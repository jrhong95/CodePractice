#   1 2 3
#   4 5 6
#   7 8 9
#   * 0 #
def solution(numbers, hand):
    keypad = [(3, 1)] + [divmod(i, 3) for i in range(9)]
    left_pos, right_pos = (3, 0), (3, 2)
    ans = ""
    for n in numbers:
        if n in [1, 4, 7]:
            ans += "L"
            left_pos = keypad[n]
        elif n in [3, 6, 9]:
            ans += "R"
            right_pos = keypad[n]
        else:
            ld = abs(keypad[n][0] - left_pos[0]) + abs(keypad[n][1] - left_pos[1])
            rd = abs(keypad[n][0] - right_pos[0]) + abs(keypad[n][1] - right_pos[1])

            if ld > rd:
                right_pos = keypad[n]
                ans += "R"
            elif ld < rd:
                left_pos = keypad[n]
                ans += "L"
            else:
                if hand == "right":
                    right_pos = keypad[n]
                    ans += "R"
                else:
                    left_pos = keypad[n]
                    ans += "L"

    return ans