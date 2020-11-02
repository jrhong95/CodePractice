def snail(snail_map):
    lst = []
    while snail_map != []:
        lst.extend(snail_map.pop(0))
        if snail_map == []:
            break     
        lst.extend([snail_map[i].pop() for i in range(len(snail_map))])
        lst.extend(snail_map.pop()[::-1])
        lst.extend([snail_map[i].pop(0) for i in range(len(snail_map))][::-1])

    return lst