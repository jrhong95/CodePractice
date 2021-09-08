def to_seconds(time):
    time = list(map(int, time.split(":")))
    return time[0] * 3600 + time[1] * 60 + time[2]


def to_time(seconds):
    hour = add_zero(seconds // 3600)
    minute = add_zero((seconds % 3600) // 60)
    second = add_zero((seconds % 3600) % 60)
    return f"{hour}:{minute}:{second}"


def add_zero(time):
    return "0" * (2 - len(str(time))) + str(time)


def solution(play_time, adv_time, logs):
    pt_second = to_seconds(play_time)
    play_time = [0] * (pt_second + 1)
    ad_time = to_seconds(adv_time)

    for log in logs:
        start, end = map(to_seconds, log.split("-"))
        play_time[start] += 1
        play_time[end] -= 1

    for i in range(1, pt_second + 1):
        play_time[i] += play_time[i - 1]

    for i in range(1, pt_second + 1):
        play_time[i] += play_time[i - 1]

    max_time, ans = play_time[ad_time - 1], 0
    for end in range(ad_time, pt_second):
        if max_time < play_time[end] - play_time[end - ad_time]:
            max_time = play_time[end] - play_time[end - ad_time]
            ans = end - ad_time + 1

    return to_time(ans)