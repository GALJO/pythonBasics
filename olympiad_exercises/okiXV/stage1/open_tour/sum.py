# https://szkopul.edu.pl/problemset/problem/Cgw52wK7lgkABFnX_GbP-kiD/site/?key=submissions - 100% points

inp = input().split()
n = int(inp[0])
x = int(inp[1])

suffix_2 = [2, 4, 8, 16, 14, 10]
suffix_6 = [6, 12]


def sum_digits(_numb):
    _numb = list(map(int, str(_numb)))
    _sum = 0
    for j in _numb:
        _sum += j
    return _sum


def get_next_el(_numb):
    return sum_digits(_numb) * 2


res = x
for i in range(n - 1):
    res = get_next_el(res)
    if res == 2:
        res = suffix_2[((n - i - 1) % 6) - 1]
        break
    elif res == 6:
        res = suffix_6[((n - i - 1) % 2) - 1]
        break
    elif res == 18:
        res = 18
        break

print(res)
