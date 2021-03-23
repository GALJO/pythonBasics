def binary_search(_tab, _x):
    # algorytm binary search napisany na podstawie zajęć ZWOJ 2021
    start = 0
    end = len(_tab) - 1
    while start < end:
        cnt = (start + end) // 2
        if _tab[cnt] < _x:
            start = cnt + 1
        else:
            end = cnt
    return start


def points_saver(_points, _p):
    _points.append(_p[0])
    _points.append(_p[1])
    return list(set(_points))


def plo():
    _points = []
    for _p in tab:
        if len(_points) == 0:
            _points = points_saver(_points, _p)
            continue

        _p_ndx = binary_search(_points, _p[0])
        if _p[0] >= _points[_p_ndx]:
            _low = _points[_p_ndx]

            if _p_ndx == len(_points) - 1:
                _up1 = n
            else:
                _up1 = _points[_p_ndx + 1]
            _up2 = _points[_p_ndx - 1]

            if _low <= _p[0] and _up1 >= _p[1]:
                _points = points_saver(_points, _p)
            elif _low <= _p[0] and _up1 <= _p[1]:
                _points = points_saver(_points, _p)
            else:
                return _p
        elif _p[0] < _points[_p_ndx]:
            _low = _points[_p_ndx - 1]

            _up1 = _points[_p_ndx]
            _up2 = _points[_p_ndx - 2]

            if _low <= _p[0] and _up1 >= _p[1]:
                _points = points_saver(_points, _p)
            elif _low >= _p[0] and _up1 <= _p[1]:
                _points = points_saver(_points, _p)
            else:
                return _p


z = int(input())
for i in range(z):
    n = int(input())
    tab = []
    for j in range(n - 2):
        tab.append(tuple(sorted(map(int, input().split()))))
        tab.sort()
    res = plo()
    print(res[0], end=' ')
    print(res[1])
