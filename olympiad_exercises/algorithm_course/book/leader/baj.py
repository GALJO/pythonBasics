def count_amount_of_items(_tab):
    _res = {}
    for _el in _tab:
        _res.setdefault(_el, 0)
        _res[_el] += 1
    return dict(sorted(_res.items(), key=lambda item: item[1]))


n = int(input())
k = list(map(int, input().split()))

am_of_items = count_amount_of_items(k)
am_of_items_k = tuple(am_of_items.keys())
leaders = (am_of_items_k[-1], am_of_items_k[-2])

possibility1 = 0
possibility2 = 0
for i in range(1, n+1):
    if i % 2 == 1:
        if k[i - 1] != leaders[0]:
            possibility1 += 1
        if k[i - 1] != leaders[1]:
            possibility2 += 1
    else:
        if k[i - 1] != leaders[1]:
            possibility1 += 1
        if k[i - 1] != leaders[0]:
            possibility2 += 1


print(min(possibility1, possibility2))