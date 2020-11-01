N = int(input()) - 1
cnt, six = 0, 666
while N != cnt:
    six += 1
    if '666' in str(six):
        cnt += 1
print(six)