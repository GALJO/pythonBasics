# https://szkopul.edu.pl/problemset/problem/Vtr5pP-RRtjqnivWocv8xaad/site/?key=statement - 100% points

def binary_search(_tab, _num):
    _start = 0
    _end = len(_tab) - 1
    while _start < _end:
        _center = (_start + _end + 1) // 2
        if int(_tab[_center]) <= _num:
            _start = _center
        else:
            _end = _center - 1
    return _start


def counter_of_longest(_tab):
    _tab.append(-1)
    _counter = 1
    _res = {}
    for _start in range(len(_tab) - 1):
        _end = _start + 1
        if _tab[_start] < _tab[_end]:
            _counter += 1
        else:
            _item = _res.get(_counter, 0)
            _res.update({_counter: _item + 1})
            _counter = 1
            continue
    return _res


def main():
    _dict_of_longest = counter_of_longest(a)
    _dol_keys = sorted(list(_dict_of_longest.keys()))
    for i in range(q):
        _active_quest = int(input())
        if _active_quest == 1:
            print(n)
            continue
        _sum = 0
        _start = binary_search(_dol_keys, _active_quest)
        for _ndx in range(_start, len(_dol_keys)):
            _len = _dol_keys[_ndx]
            _occur = _dict_of_longest.get(_len)
            if _len >= _active_quest:
                _sum += (_len - _active_quest + 1) * _occur
        print(_sum)


n = int(input())
a = list(map(int, input().split()))
q = int(input())
main()
