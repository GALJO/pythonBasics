# https://szkopul.edu.pl/problemset/problem/EoHxXpP-oYOLwSqFmAfGQJvW/site/?key=statement - 100% points

def count_price(_numb_of_house):
    _prize = 0
    for _numb in _numb_of_house:
        _prize += _numb
    return _prize


def find_start_ndx(_arr):
    if len(str(a)) < len(str(b)):
        return 0
    _res = 0
    for _i in range(len(_arr)):
        if _arr[_i] > int(str(a)[_i]):
            _res = _i
            break
    return _res


def calc_house_price():
    if a == b:
        return count_price(list(map(int, str(a))))
    _house_numb = list(map(int, str(b)))
    if _house_numb == [9] * len(_house_numb):
        return count_price(_house_numb)

    start = find_start_ndx(_house_numb)
    _house_numb[start] -= 1
    for _i in range(1, len(_house_numb)):
        if _i <= start:
            continue
        _house_numb[_i] = 9
    _res = count_price(_house_numb)
    return _res


ab = input().split()
a, b = int(ab[0]), int(ab[1])
print(calc_house_price())
