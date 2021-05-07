import re


def step1(id):
    return id.lower()


def step2(id):
    ids = re.compile(r'[-.\w]').findall(id)
    return "".join(ids) if ids else "a"


def step3(id):
    id = re.sub(r'\.{1,}', '.', id)
    return id if id else "a"


def step4(id):
    if id and id[0] == '.':
        id = id[1:]
    if id and id[-1] == '.':
        id = id[:-1]
    return id if id else 'a'


def step6(id):
    return id[:15] if len(id) > 15 else id


def step7(id):
    if len(id) < 3:
        while len(id) < 3:
            id += id[-1]
    return id


def solution(id):
    id = step1(id)
    id = step2(id)
    id = step3(id)
    id = step4(id)
    id = step6(id)
    id = step4(id)
    return step7(id)


print(solution(	"abcdefghijklmn.p"))
