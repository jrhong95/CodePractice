from collections import deque

# 1. 다리에 들어갈 수 잇는지 검사
# 2. 들어갈 수 있으면 on_bridge에서 pop(0)하고 append(w)
# 3. 들어갈 수 없으면 그냥 넘김
# 4. 시간 += 1


def solution(bridge_length, weight, truck_weights):
    on_bridge, sum_bridge, time = [0] * bridge_length, 0, 0

    while truck_weights:
        sum_bridge -= on_bridge.pop(0)

        if sum_bridge + truck_weights[0] <= weight:
            sum_bridge += truck_weights[0]
            on_bridge.append(truck_weights.pop(0))

        else:
            on_bridge.append(0)

        time += 1

    while on_bridge:
        on_bridge.pop(0)
        time += 1

    return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100,	100, [10]))
print(solution(100,	100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]	))
