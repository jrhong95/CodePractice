def solution(files):
    split_files = []
    for file in files:
        num_start, num_end, num_flag = 0, 0, False
        for i, c in enumerate(file):
            if c.isdigit() and not num_flag:
                num_start = i
                num_flag = True
            elif num_flag and not c.isdigit():
                num_end = i
                num_flag = False
                break
        if num_flag:
            num_end = len(file)
            split_files.append((file[:num_start], file[num_start:num_end], ""))
        else:
            split_files.append(
                (file[:num_start], file[num_start:num_end], file[num_end:])
            )

    return [
        "".join(x) for x in sorted(split_files, key=lambda x: (x[0].lower(), int(x[1])))
    ]
