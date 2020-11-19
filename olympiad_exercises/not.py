def search_growth_series(_tab, _length_of_series):
    _count = 0
    for _i in range(len(_tab) - _length_of_series + 1):
        for _j in range(_i, _i + _length_of_series - 1):
            if _tab[_j] < _tab[_j + 1]:
                if _j == _i + _length_of_series - 2:
                    _count += 1
                continue
            else:
                break
    return _count


n = int(input())
a = list(map(int, input().split()))
q = int(input())

results = []
for i in range(q):
    active_quest = int(input())
    if active_quest == 1:
        results.append(n)
        continue

    results.append(search_growth_series(a, active_quest))

for result in results:
    print(result)
