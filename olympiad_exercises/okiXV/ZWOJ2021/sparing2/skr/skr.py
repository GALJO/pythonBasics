def skr():
    _sum = 0
    for _j in range(k, n):
        _sum += A[_j]
    print(max(A[0], _sum))


nk = input().split()
n = int(nk[0])
k = int(nk[1])
A = list(sorted(map(int, input().split()), reverse=True))

skr()