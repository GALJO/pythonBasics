def test_tape(_draft):
    _max = len(_draft)
    _start = _draft[0]
    _next = 0

    for _i in range(1, len(_draft)):
        if _start < _max:
            _next = _start + 1
            _start = _next
        else:
            _next = 1
            _start = 1

        if _draft[_i] == _next:
            continue
        else:
            return 0
    return 1


def tas():
    for _i in range(0, n):
        for _j in range(_i + 1, n):
            _draft = A.copy()
            _draft[_i:_j + 1] = reversed(_draft[_i:_j + 1])
            _test = test_tape(_draft)
            if _test:
                return 'TAK'
    return 'NIE'


n = int(input())
A = list(map(int, input().split()))

print(tas())
