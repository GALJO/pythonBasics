nm = input().split()
n, m = int(nm[0]), int(nm[1])
a = list(map(int, input().split()))

_can_jump = False
for i in range(m):
    if a[i] == n:
        _can_jump = True
        print(i + 1)
        break

if not _can_jump:
    print(-1)
