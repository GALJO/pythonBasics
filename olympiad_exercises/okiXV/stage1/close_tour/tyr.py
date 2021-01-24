def main():
    """
    Znajduje dwa punkty, miedzy ktorymi jest najmniejsze nachylenie.
    Uzywa wzoru na nachylenie (|yi - yj|) / (|xi - xy|).
    :return: tablica dwoch wspolrzednych
    """
    _res = []
    _res_value = -1
    for _i in range(n):
        for _j in range(_i, n):
            if _j == _i:
                continue
            _tilt = (abs(points[_i][1] - points[_j][1])) / (abs(points[_i][0] - points[_j][0]))
            if _tilt == 0.0:
                continue
            if _tilt < _res_value or _res_value == -1:
                _res_value = _tilt
                _res = [_i + 1, _j + 1]
    return _res


n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

results = main()
for res in results:
    print(res, end=' ')
