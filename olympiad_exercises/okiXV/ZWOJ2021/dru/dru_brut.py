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


def find_power_of_draw(_end_ndx, _tab):
    _res = 1
    _start_ndx = binary_search(_tab, _tab[_end_ndx][0])
    _start_ndx = repair_binary_search(_tab, _start_ndx)
    for _i in range(_start_ndx, _end_ndx):
        if _tab[_end_ndx].startswith(_tab[_i]):
            _res += 1
    return _res


n = int(input())
sheets = []
for i in range(n):
    sheets.append(input())
sheets.sort()

powers = [1]
for i in range(1, n):
    if not sheets[i].startswith(sheets[i - 1]):
        powers.append(find_power_of_draw(i - 1, sheets))
    if i == n - 1:
        powers.append(find_power_of_draw(i, sheets))
        break

print(max(powers))
