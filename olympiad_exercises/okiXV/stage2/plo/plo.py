def find_biggest_connection(_tab):
    if not _tab:
        return []
    _first = _tab[-1][0]
    for _i in range(len(_tab) - 1, -1, -1):
        if _tab[_i][0] != _first:
            return _tab[_i + 1]
    return _tab[0]


def count_inputs_and_outputs(_connects):
    _inputs = {}
    _outputs = {}
    _keys = set()
    for _connect in _connects:
        _inputs.setdefault(_connect[1], [])
        _outputs.setdefault(_connect[0], [])
        _inputs[_connect[1]].append(_connect[0])
        _outputs[_connect[0]].append(_connect[1])
        _keys.add(_connect[0])
        _keys.add(_connect[1])
    _keys = sorted(list(_keys))
    return _inputs, _outputs, _keys


def optimize_open_connects(_tab, _top, _inputs):
    _inputs.setdefault(_top, False)
    if _inputs[_top]:
        for _i in range(len(_inputs[_top])):
            _actual_connect = sorted([_inputs[_top][_i], _top])
            _tab.remove(_actual_connect)
        _tab.sort()
    return _tab


def test_sus_connects(_top, _outputs, _opened_connects):
    _biggest_connect = find_biggest_connection(_opened_connects)
    _outputs.setdefault(_top, False)

    if _outputs[_top]:
        for _i in range(len(_outputs[_top])):
            _actual_connect = sorted([_top, _outputs[_top][_i]])
            if _opened_connects and _biggest_connect and \
                    _biggest_connect[0] < _actual_connect[0] and _biggest_connect[1] < _actual_connect[1]:
                return _opened_connects, [_biggest_connect, _actual_connect]
            else:
                _opened_connects.append(_actual_connect)
                _opened_connects.sort()
    return _opened_connects, None


def find_intersection(_connects, _tops_amount):
    _opened_connects = []
    _in, _out, _keys = count_inputs_and_outputs(_connects)

    for _i in range(len(_out[_keys[0]])):
        _opened_connects.append([_keys[0], _out[_keys[0]][_i]])
    _opened_connects.sort()
    _keys.pop(0)

    for _top in _keys:
        _opened_connects = optimize_open_connects(_opened_connects, _top, _in)
        _opened_connects, _dangerous_connects = test_sus_connects(_top, _out, _opened_connects)
        if _dangerous_connects is not None:
            return _dangerous_connects
    return None


z = int(input())
for i in range(z):
    n = int(input())
    tab = []
    for j in range(n - 2):
        actual_tuple = list(sorted(map(int, input().split())))
        tab.append(actual_tuple)
    tab.sort()

    dangerous_connects = find_intersection(tab, n)
    amount_of_tops = n
    tested_connect = dangerous_connects[1]
    tab.remove(dangerous_connects[1])
    if find_intersection(tab, n) is None:
        print('{} {}'.format(tested_connect[0], tested_connect[1]))
    else:
        print('{} {}'.format(dangerous_connects[0][0], dangerous_connects[0][1]))
