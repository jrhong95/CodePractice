import sys
read = sys.stdin.readline

N, M = map(int, read().split())
lier = list(map(int, read().split()))

if len(lier) == 1:
    parties = [read() for _ in range(M)]
    print(M)
else:
    liers = set(lier[1:])

    lier_add = True
    parties = [list(map(int, read().split()))[1:] for _ in range(M)]
    new_party = parties[:]

    while lier_add:
        lier_add = False
        parties = new_party[:]
        new_party = []
        for cur_party in parties:
            is_lier = False
            for c in cur_party:
                if c in liers:
                    liers.update(cur_party)
                    lier_add = True
                    is_lier = True

            if not is_lier:
                new_party.append(cur_party)

    print(len(new_party))
