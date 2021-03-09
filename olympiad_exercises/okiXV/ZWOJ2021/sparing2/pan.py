def find_dividers(_x):
    _res = []
    for _i in range(1, int(_x / 2) + 1):
        if _x % _i == 0:
            _res.append(_i)
    _res.append(_x)
    return _res


def binary_search(_tab, _x):
    start = 0
    end = len(_tab) - 1
    while start < end:
        cnt = (start + end) // 2
        if _tab[cnt] < _x:
            start = cnt + 1
        else:
            end = cnt
    return start


def is_sum(_tab, _numb, _start_ndx):
    _sum = _numb
    for _i in range(_start_ndx, -1, -1):
        if _sum - _tab[_i] > 0:
            _sum -= _tab[_i]
        elif _sum - _tab[_i] == 0:
            return True
    return False


def pan():
    for _i in range(z):
        _actual_quest = quests[_i]
        _dividers = find_dividers(_actual_quest)
        _is_sum = True
        for _j in range(1, _actual_quest + 1):
            _j_ndx = binary_search(_dividers, _j)
            if _dividers[_j_ndx] == _j:
                continue
            _actual_draft = _dividers[0:_j_ndx + 1]
            if not is_sum(_actual_draft, _j, _j_ndx):
                print('NIE')
                _is_sum = False
                break
        if _is_sum:
            print('TAK')


z = int(input())
quests = []
for i in range(z):
    quests.append(int(input()))

pan()
