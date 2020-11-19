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
list_of_longest = counter_of_longest(a)
lol_items = list_of_longest.items()
for i in range(q):
    active_quest = int(input())
    if active_quest == 1:
        print(n)
        continue
    sum_ = 0
    for lo in lol_items:
        if lo[0] >= active_quest:
            sum_ += (lo[0] - active_quest + 1) * lo[1]
    print(sum_)