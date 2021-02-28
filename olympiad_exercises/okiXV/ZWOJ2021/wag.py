def count_results(_tab):
    _res = {}
    for _i in range(len(_tab)):
        _value = _tab[_i][0] / (2 ** _tab[_i][1])
        _res.setdefault(_value, [])
        _res[_value].append(_tab[_i])
    return _res


def count_order(_dict):
    _res = []
    _items = dict(sorted(_dict.items()))
    _items_keys = list(_items.keys())
    for _i in range(len(_items_keys)):
        _actual_value = _items[_items_keys[_i]]
        if len(_actual_value) > 1:
            _actual_value.sort()
            for _j in range(len(_actual_value)):
                _res.append(_actual_value[_j])
        else:
            _res.append(_actual_value[0])
    return _res


n = int(input())
A = []

for i in range(n):
    A.append(list(map(int, input().split())))

results = count_results(A)
res = count_order(results)

for i in range(len(res)):
    print(res[i][0], end=' ')
    print(res[i][1])
