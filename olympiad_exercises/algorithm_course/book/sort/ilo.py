z = int(input())
for i in range(z):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[0] * a[1] * a[2])
