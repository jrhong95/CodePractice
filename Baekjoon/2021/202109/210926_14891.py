import sys
from collections import deque

read = sys.stdin.readline

gears = [deque(list(read().rstrip())) for _ in range(4)]
commands = [list(map(int, read().split())) for _ in range(int(read()))]
LEFT, RIGHT = -2, 2


def rotate(direction, gear_num, flags):
    flags[gear_num] = True

    if direction == 1:  # 시계방향
        if (  # 왼쪽기어가 돌 수 있으면
            gear_num - 1 >= 0
            and not flags[gear_num - 1]
            and gears[gear_num][LEFT] != gears[gear_num - 1][RIGHT]
        ):
            rotate(-1, gear_num - 1, flags)

        if (  # 오른쪽 기어가 돌 수 있으면
            gear_num + 1 < 4
            and not flags[gear_num + 1]
            and gears[gear_num][RIGHT] != gears[gear_num + 1][LEFT]
        ):
            rotate(-1, gear_num + 1, flags)

        gears[gear_num].appendleft(gears[gear_num].pop())
    else:
        if (  # 왼쪽기어가 돌 수 있으면
            gear_num - 1 >= 0
            and not flags[gear_num - 1]
            and gears[gear_num][LEFT] != gears[gear_num - 1][RIGHT]
        ):
            rotate(1, gear_num - 1, flags)

        if (  # 오른쪽 기어가 돌 수 있으면
            gear_num + 1 < 4
            and not flags[gear_num + 1]
            and gears[gear_num][RIGHT] != gears[gear_num + 1][LEFT]
        ):
            rotate(1, gear_num + 1, flags)

        gears[gear_num].append(gears[gear_num].popleft())


def main():
    for gear, dir in commands:
        rotate(dir, gear - 1, [False, False, False, False])
    print(sum(int(gears[i][0]) * (2 ** i) for i in range(4)))


main()