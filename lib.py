import random
import math


def is_int(el):
    try:
        el = int(el)
    except ValueError:
        return False
    return True


def power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        s = power(x, n / 2)
        return s * s
    else:
        s = power(x, n - 1)
        return x * s


def random_number(_min, _max, am):
    res = []
    for i in range(am):
        res.append(int(random.random() * (_max - _min) + _min))
    return res


def binary_search_lower_bound(_tab, _x):
    start = 0
    end = len(_tab) - 1
    while start < end:
        cnt = (start + end) // 2
        if _tab[cnt] < _x:
            start = cnt + 1
        else:
            end = cnt
    return start


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


def eratostenes_sieve(_numb):
    first_dividers = []
    for i in range(_numb + 1):
        first_dividers.append(0)
    first_dividers[0] = 1
    first_dividers[1] = 1
    for j in range(2, _numb + 1):
        if first_dividers[j] != 0:
            continue
        if first_dividers[j] == 0:
            first_dividers[j] = j
            for x in range(j * 2, _numb + 1, j):
                if first_dividers[x] == 0:
                    first_dividers[x] = j
    return first_dividers


def prefix_sum(_tab):
    _pref = [0]
    for _i in range(0, len(_tab)):
        _pref.append(_pref[_i] + _tab[_i])
    return _pref


def sum_of_list(_list):
    _sum = 0
    for _i in range(len(_list)):
        _sum += _list[_i]
    return _sum
