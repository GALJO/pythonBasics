import random


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
