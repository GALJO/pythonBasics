# https://szkopul.edu.pl/problemset/problem/KFZaiUOIU7YpOYeKtRE47g1G/site/?key=statement - 100% points

def main():
    _res = 1
    _i = 1
    while _i < n:
        if P[_i - 1] <= P[_i]:
            _i += 1
            continue
        else:
            _res += 1
            _j = _i
            while _j < n:
                if P[_j - 1] >= P[_j]:
                    _j += 1
                    continue
                else:
                    _res += 1
                    _i = _j
                    break
            _i = _j
        _i += 1
    return _res


n = int(input())
P = list(map(int, input().split()))
print(main())
