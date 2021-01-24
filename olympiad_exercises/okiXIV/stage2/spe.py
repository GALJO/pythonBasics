def find_path(_lvl, _next_levels):
    _done = [0] * n
    _path = []
    while _done[_lvl - 1] == 0:
        _path.append(_lvl)
        _done[_lvl - 1] = 1
        _lvl = T[_lvl - 1]
    return _path


def _sum_path(_path):
    _res = 0
    for _el in _path:
        _res += _el
    return _res


def find_shortest_time(_times):
    _res = -1
    for _time in _times:
        if _res > _time:
            _res = _time
        elif _res == -1:
            _res = _time
    return _res


def main():
    _times = {}
    for _i in range(1, n + 1):
        _times.setdefault(_i, -1)
        if _times[_i] == -1:
            _act_path = find_path(_i, T)
            _sum = _sum_path(_act_path)
            for _el in range(len(_act_path)):
                _times.setdefault(_act_path[_el], -1)
                if _times[_act_path[_el]] == -1:
                    if _el - 1 == -1:
                        _times[_act_path[_el]] = _sum
                    else:
                        _times[_act_path[_el]] = _times[_act_path[_el - 1]] - _act_path[_el - 1]
    return find_shortest_time(_times.values())


n = int(input())
T = list(map(int, input().split()))
print(main())
