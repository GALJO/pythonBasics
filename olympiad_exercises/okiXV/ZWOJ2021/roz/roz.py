def make_pairs(_numbs):
    _pairs = []
    _prev = None
    for _el in _numbs:
        if _prev is None:
            _prev = _el
            continue
        _pairs.append((_prev, _el))
        _prev = _el
    _pairs.sort()
    return _pairs


def binary_search(_tab, _x):
    start = 0
    end = len(_tab) - 1
    while start < end:
        cnt = (start + end) // 2
        if _tab[cnt][0] < _x:
            start = cnt + 1
        else:
            end = cnt
    return start


def count_power(_pairs, _rainfall, _dict):
    _start = binary_search(_pairs, _rainfall[0])
    for _i in range(_start, len(_pairs)):
        if _rainfall[1] < _pairs[_i][0]:
            break
        if _rainfall[0] <= _pairs[_i][0] and _rainfall[1] >= _pairs[_i][1]:
            _dict.setdefault(_pairs[_i], 0)
            _dict[_pairs[_i]] += 1


n = int(input())
rainfalls = []
first_numbers = {-1}
second_numbers = {-1}
for i in range(n):
    actual_tuple = tuple(map(int, input().split()))
    rainfalls.append(actual_tuple)
    first_numbers.add(actual_tuple[0])
    second_numbers.add(actual_tuple[1])
first_numbers.remove(-1)
second_numbers.remove(-1)
numbers = list(first_numbers) + list(second_numbers)
rainfalls.sort()
numbers.sort()

if len(numbers) == 1:
    print(len(rainfalls))
else:
    pairs = make_pairs(numbers)
    powers = {}
    for rainfall in rainfalls:
        count_power(pairs, rainfall, powers)

    print(max(powers.values()))
