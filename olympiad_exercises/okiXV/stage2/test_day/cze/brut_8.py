# https://szkopul.edu.pl/problemset/problem/aQmcC7zKJ25u8GHcjaCv49e4/site/?key=submissions - 8% points

def find_dividers(_x):
    _res = []
    for _i in range(1, int(_x / 2) + 1):
        if _x % _i == 0:
            _res.append(_i)
    _res.append(_x)
    return _res


def make_pairs(_dividers):
    _res = []
    while len(_dividers) > 0:
        if len(_dividers) == 1:
            _res.append((_dividers[0], _dividers[0]))
            _dividers.pop(0)
        else:
            _res.append((_dividers[0], _dividers[len(_dividers) - 1]))
            _dividers.pop(0)
            _dividers.pop(len(_dividers) - 1)
    return _res


def cze():
    for pair in pairs:
        if pair[0] <= a and pair[1] <= b:
            return 'TAK'
        elif pair[0] <= b and pair[1] <= a:
            return 'TAK'
        else:
            continue
    return 'NIE'


abcd = input().split()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

amount_of_cubes = c * d
dividers = find_dividers(amount_of_cubes)
pairs = make_pairs(dividers)

print(cze())