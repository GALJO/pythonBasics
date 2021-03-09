def count_cords(_moves, _snake_len):
    _cords = [[(0, 0)]]
    for _i in range(len(_moves)):
        _cords.append([])
        if _moves[_i] == 'N':
            _cords[_i + 1].append((_cords[_i][0][0] - 1, _cords[_i][0][1]))
            for _j in range(len(_cords[_i])):
                _cords[_i + 1].append(_cords[_i][_j])
        elif _moves[_i] == 'S':
            _cords[_i + 1].append((_cords[_i][0][0] + 1, _cords[_i][0][1]))
            for _j in range(len(_cords[_i])):
                _cords[_i + 1].append(_cords[_i][_j])
        elif _moves[_i] == 'E':
            _cords[_i + 1].append((_cords[_i][0][0], _cords[_i][0][1] + 1))
            for _j in range(len(_cords[_i])):
                _cords[_i + 1].append(_cords[_i][_j])
        elif _moves[_i] == 'W':
            _cords[_i + 1].append((_cords[_i][0][0], _cords[_i][0][1] - 1))
            for _j in range(len(_cords[_i])):
                _cords[_i + 1].append(_cords[_i][_j])
        if len(_cords[_i + 1]) > _snake_len:
            _cords[_i + 1].pop(-1)
    return _cords


def waz():
    _cords = count_cords(M, m)
    _res = [0] * n
    for _i in range(1, len(_cords)):
        _actual_position = _cords[_i]
        for _j in range(len(_actual_position)):
            _actual_cords = _actual_position[_j]
            _cords_color = P[_actual_cords[0]][_actual_cords[1]]
            if _j + 1 == _cords_color:
                _res[_i - 1] += 1
    return _res


ab = input().split()
a, b = int(ab[0]), int(ab[1])
P = []
for i in range(a):
    P.append(tuple(map(int, input().split())))
nm = input().split()
n, m = int(nm[0]), int(nm[1])
M = tuple(map(str, input()))

result = waz()
for numb in result:
    print(numb, end=' ')