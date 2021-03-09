def main():
    _biggest_score = 0
    for _i in range(n):
        _sum = 0
        _numbers = []
        for _j in range(_i, n):
            _sum += A[_j]
            _numbers.append(A[_j])
            if _sum * sorted(_numbers)[0] > _biggest_score:
                _biggest_score = _sum * sorted(_numbers)[0]
    return _biggest_score


n = int(input())
A = tuple(map(int, input().split()))

print(main())
