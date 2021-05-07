def solution(array, commands):
    ans = []
    for command in commands:
        i, j, k = command
        arr = sorted(array[i - 1: j])
        ans.append(arr[k - 1])
    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
