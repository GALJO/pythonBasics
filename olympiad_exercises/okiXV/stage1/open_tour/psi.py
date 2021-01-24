n = int(input())
c = list(map(int, input().split()))


def find_first_series_start(_tab, _second_start_index):
    _res = 0
    _sum = 0
    _isFirstEven = _tab[0] % 2 == 0
    if not _isFirstEven:
        _second_start_index = 1
    for i in range(0, len(_tab)):
        _sum += _tab[i]
        if _sum % 2 == 0:
            _res += 1
        if _second_start_index == -1 and _isFirstEven and _tab[i] % 2 == 1:
            _second_start_index = i + 1
    return _res, _second_start_index


def find_second_series_start(_tab, _index):
    _res = 0
    _sum = 0
    if _index == -1:
        return 0
    for i in range(_index, len(_tab)):
        _sum += _tab[i]
        if _sum % 2 == 0:
            _res += 1
    return _res


def count_series(_series_start1, _series_start2):
    _res = 0
    for _i in range(1, _series_start1 + 1):
        _res += _i
    for _i in range(1, _series_start2 + 1):
        _res += _i
    return _res


second_start_index = -1
first_start, second_start_index = find_first_series_start(c, second_start_index)
second_start = find_second_series_start(c, second_start_index)
print(count_series(first_start, second_start))
