import sys

read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
indices = []
lis_list = []


def binary_search(num):
    start, end = 0, len(lis_list) - 1

    while start < end:
        mid = (start + end) // 2

        if lis_list[mid] >= num:
            end = mid
        else:
            start = mid + 1

    return start


def main():
    for i, num in enumerate(nums):
        if not lis_list or lis_list[-1] < num:
            indices.append(len(lis_list))
            lis_list.append(num)
        else:
            idx = binary_search(num)
            indices.append(idx)
            lis_list[idx] = num

    ans = []
    size = len(lis_list) - 1
    for i in range(N - 1, -1, -1):
        if indices[i] == size:
            ans.append(nums[i])
            size -= 1
        if size == -1:
            break

    print(len(ans))
    print(*ans[::-1])


main()
