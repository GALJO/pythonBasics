def find_uniques(_tab, _len):
    _dict = {}
    for _i in range(_len):
        if _tab[_i] in _dict:
            _dict[_tab[_i]] = -1
        else:
            _dict.setdefault(_tab[_i], _i)
    _values = list(_dict.values())
    _values = list(dict.fromkeys(_values))
    _values.pop(0)
    return _values


def is_series_boring(_series):
    _len = len(_series)
    for _i in range(_len):
        _dict = {_series[_i]: 1}
        for _j in range(_i + 1, _len):
            _dict.setdefault(_series[_j], 0)
            _dict[_series[_j]] += 1
            if is_boring(_dict):
                return True
    return False


def is_boring(_dict):
    _keys = list(_dict.keys())
    for _i in range(len(_dict)):
        if _dict[_keys[_i]] == 1:
            return False
    return True


def cie(_series, _series_len):
    _unique_ndx = find_uniques(_series, _series_len)
    if len(_unique_ndx) == 0:
        return 'nudny'

    _unique_ndx.append(len(_series))
    _first_ndx = 0
    for _last_ndx in _unique_ndx:
        if is_series_boring(_series[_first_ndx:_last_ndx]):
            return 'nudny'
        _first_ndx = _last_ndx + 1
    return 'ciekawy'


z = int(input())
quests = []
for i in range(z):
    quests.append(int(input()))
    quests.append(tuple(map(int, input().split())))

for q in range(0, len(quests) - 1, 2):
    series = quests[q + 1]
    series_len = quests[q]
    print(cie(series, series_len))
