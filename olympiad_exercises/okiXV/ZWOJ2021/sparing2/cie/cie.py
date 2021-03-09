def search_uniques(_tab):
    _dict = {}
    _res = []
    for _i in range(len(_tab)):
        _dict.setdefault(_tab[_i], 0)
        _dict[_tab[_i]] += 1
    for _i in range(len(_tab)):
        if _dict[_tab[_i]] == 1:
            _res.append(_tab[_i])
    return _res


def is_boring(_dict):
    _keys = list(_dict.keys())
    for _i in range(len(_dict)):
        if _dict[_keys[_i]] == 1:
            return False
    return True


def cie():
    for _q in range(0, len(quests) - 1, 2):
        _actual_quest = quests[_q + 1]
        _is_boring = False
        for _i in range(quests[_q]):
            if _is_boring:
                break
            _dict = {_actual_quest[_i]: 1}
            for _j in range(_i + 1, quests[_q]):
                _dict.setdefault(_actual_quest[_j], 0)
                _dict[_actual_quest[_j]] += 1
                if is_boring(_dict):
                    print('nudny')
                    _is_boring = True
                    break
        if not _is_boring:
            print('ciekawy')


z = int(input())
quests = []
for i in range(z):
    quests.append(int(input()))
    quests.append(tuple(map(int, input().split())))

cie()
