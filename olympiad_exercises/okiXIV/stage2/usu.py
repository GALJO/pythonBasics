def make_help_sums(_tab):
    _res = []
    for _i in range(len(_tab)):
        _actual_box = _tab[_i]
        if len(_tab) - _i <= _actual_box:
            _res.append(len(_tab) - _i)
        else:
            _res.append(_actual_box)
    return _res


def _find_biggest_numb(_tab):
    return sorted(_tab)[-1]


def reduce_tab(_tab, _start):
    _reduced_tab = _tab[0:_start]
    return _reduced_tab


def main():
    _t = T
    _help_sums = make_help_sums(_t)
    _amount_of_moves = 0
    while len(_t) != 0:
        _biggest_help_sum = _find_biggest_numb(_help_sums)
        for _i in range(len(_t)):
            if _help_sums[_i] == _biggest_help_sum:
                _t = reduce_tab(_t, _i)
                _help_sums = reduce_tab(_help_sums, _i)
                _amount_of_moves += 1
                break
    return _amount_of_moves


n = int(input())
T = list(map(int, input().split()))
print(main())