def binary_search(_tab, _str):
    _start = 0
    _end = len(_tab) - 1
    while _start < _end:
        _cnt = (_start + _end + 1) // 2
        if _tab[_cnt] <= _str:
            _start = _cnt
        else:
            _end = _cnt - 1
    return _start


def repair_binary_search(_tab, _ndx):
    _res = _ndx
    for _i in range(_ndx, -1, -1):
        if _tab[_ndx] == _tab[_i]:
            _res = _i
        else:
            break
    return _res


def find_power_of_draw(_tab, _start_ndx, _powers):
    _res = 1
    for _i in range(_start_ndx, -1, -1):
        if not _tab[_i].startswith(_tab[_start_ndx + 1][0]):
            break
        if _tab[_start_ndx + 1].startswith(_tab[_i]):
            _res += _powers[_i]
            break
    return _res


n = int(input())
sheets = []
for i in range(n):
    sheets.append(input())
sheets.sort()

powers = [1]
for i in range(1, n):
    if sheets[i].startswith(sheets[i - 1]):
        powers.append(powers[i - 1] + 1)
    else:
        powers.append(find_power_of_draw(sheets, i - 1, powers))

print(max(powers))
