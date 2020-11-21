def find_the_best(_tab, _num):
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
            item = _res.get(_counter, 0)
            _res.update({_counter: item + 1})
            _counter = 1
            continue
    return _res


n = int(input())
a = list(map(int, input().split()))
q = int(input())

results = []
dict_of_longest = counter_of_longest(a)
dol_keys = sorted(list(dict_of_longest.keys()))
for i in range(q):
    active_quest = int(input())
    if active_quest == 1:
        print(n)
        continue
    sum_ = 0
    start = find_the_best(dol_keys, active_quest)
    for ndx in range(start, len(dol_keys)):
        length = dol_keys[ndx]
        occur = dict_of_longest.get(length)
        if length >= active_quest:
            sum_ += (length - active_quest + 1) * occur
    print(sum_)
