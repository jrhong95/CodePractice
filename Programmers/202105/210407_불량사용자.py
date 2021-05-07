from itertools import permutations


def check(users, bans):
    for i in range(len(bans)):
        if len(users[i]) != len(bans[i]):
            return False

        for j in range(len(users[i])):
            if bans[i][j] != "*" and bans[i][j] != users[i][j]:
                return False

    return True


def solution(user_id, banned_id):
    ans = []

    for users in permutations(user_id, len(banned_id)):
        if check(users, banned_id):
            users = set(users)
            if users not in ans:
                ans.append(users)

    return len(ans)
