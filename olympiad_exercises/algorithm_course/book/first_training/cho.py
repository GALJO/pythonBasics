n = int(input())
numbs = list(map(int, input().split()))
numbs.sort()
for i in range(1, n):
    if numbs[i - 1] != i:
        print(i)
        break

