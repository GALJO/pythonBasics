def sum_of_list(_list):
    _sum = 0
    for _i in range(len(_list)):
        _sum += _list[_i]
    return _sum

n = int(input())
a = list(map(int, input().split()))

results = []
part_one = 0
part_two = sum_of_list(a)
results.append(part_one - part_two)
for i in range(1, n):
    part_one += a[i]
    part_two -= a[i]
    results.append(part_one - part_two)

print(min((abs(x), x) for x in results)[1])
