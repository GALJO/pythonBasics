import math


def make_sum_of_list(_list):
    _sum = 0
    for _i in range(len(_list)):
        _sum += _list[_i]
    return _sum


def compare_parts(_part1, _part2):
    _final = []
    for _i in range(0, len(_part2)):
        if i > len(_part1):
            _final.append(_part1[_i])
        if _i < len(_part2):
            _final.append(_part2[_i])
    return _final


def count_isolation_level(_isolations, _sum):
    _res = _sum
    for _i in range(len(_isolations)):
        if _isolations[_i - 1] < _isolations[_i] and _i != 0:
            _res += _isolations[_i] - _isolations[_i - 1]
    return _res


n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

a_sum = make_sum_of_list(A)
sorted_a = sorted(A)
a_part1 = sorted_a[0:math.floor(len(sorted_a) / 2)]
a_part1.sort(reverse=True)
a_part2 = sorted_a[math.ceil(len(sorted_a) / 2):len(sorted_a)]
final_a = compare_parts(a_part1, a_part2)
res = count_isolation_level(final_a, a_sum)
print(res)