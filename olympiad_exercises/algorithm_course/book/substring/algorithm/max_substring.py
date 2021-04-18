def max_substring_value(_tab):
    _w = [0] * len(_tab)
    _w[-1] = _tab[-1]
    for _i in range(len(_tab) - 2, -1, -1):
        _w[_i] = max(_w[_i + 1] + _tab[_i], _tab[_i])
    return max(_w)


a = tuple(map(int, input().split()))

print(max_substring_value(a))
