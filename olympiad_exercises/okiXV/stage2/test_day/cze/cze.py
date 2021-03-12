# https://szkopul.edu.pl/problemset/problem/aQmcC7zKJ25u8GHcjaCv49e4/site/?key=submissions - 100% points

import math


def find_dividers(_x):
    _small_dividers = []
    _big_dividers = []
    if _x == 1:
        return [1]
    for _i in range(1, math.ceil(math.sqrt(_x)) + 1):
        if _x % _i == 0:
            _small_dividers.append(_i)
            _big_dividers.append(_x // _i)
    _res = _small_dividers + list(reversed(_big_dividers))
    return _res


def make_dividers(_tab1, _tab2):
    if _tab1 >= _tab2:
        _first = _tab1
        _last = _tab2
    else:
        _first = _tab2
        _last = _tab1
    _res = []
    for i in range(len(_first)):
        for j in range(len(_last)):
            _res.append(_first[i] * _last[j])
    _res = set(_res)
    _res = list(_res)
    _res.sort()
    return _res


def make_pairs(_dividers):
    _res = []
    while len(_dividers) > 0:
        if len(_dividers) == 1:
            _res.append((_dividers[0], _dividers[0]))
            _dividers.pop(0)
        else:
            _res.append((_dividers[0], _dividers[len(_dividers) - 1]))
            _dividers.pop(0)
            _dividers.pop(len(_dividers) - 1)
    return _res


def cze():
    for pair in pairs:
        if pair[0] <= a and pair[1] <= b:
            return 'TAK'
        elif pair[0] <= b and pair[1] <= a:
            return 'TAK'
        else:
            continue
    return 'NIE'


abcd = input().split()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

dividers_c = find_dividers(c)
dividers_d = find_dividers(d)
dividers = make_dividers(dividers_c, dividers_d)
pairs = make_pairs(dividers)

print(cze())
