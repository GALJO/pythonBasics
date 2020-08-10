def sum_n(_n):
    _sum_n = 0
    for i in range(_n + 1):
        _sum_n += i
    return _sum_n


def print_result(_x, _n):
    for i in range(_n):
        print(int(x) + i, end=' ')


numbs = input().split()

n = int(numbs[0])
s = int(numbs[1])

x = (s - sum_n(n - 1)) / n

if x == round(x):
    print_result(x, n)
else:
    print('NIE')
