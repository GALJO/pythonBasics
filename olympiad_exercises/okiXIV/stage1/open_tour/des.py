n = int(input())
L = list(sorted(map(int, input().split())))

if n < 4:
    print(0)
else:
    _res = L[-4] * L[-4]
    print(_res)