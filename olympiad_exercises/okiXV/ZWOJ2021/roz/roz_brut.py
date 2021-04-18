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


def count_power(_rainfalls, _pair):
    _power = 0
    for _i in range(len(_rainfalls)):
        if _rainfalls[_i][0] > _pair[1]:
            break
        if _rainfalls[_i][1] >= _pair[1] and _rainfalls[_i][0] <= _pair[0]:
            _power += 1
    return _power


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
    powers = []
    for pair in pairs:
        powers.append(count_power(rainfalls, pair))

    print(max(powers))
