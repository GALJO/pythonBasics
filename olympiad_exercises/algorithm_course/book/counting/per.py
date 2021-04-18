n = int(input())
a = list(map(int, input().split()))
a.sort()

is_ = True
for i in range(1, n + 1):
    if i != a[i - 1]:
        is_ = False
        break


if is_:
    print('TAK')
else:
    print('NIE')


