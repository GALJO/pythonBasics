n = int(input())
coord = []
for i in range(n):
    coord.append(tuple(map(int, input().split())))
coord.sort()

res = -1
for i in range(0, n - 1):
    if res == 1:
        break
    dist = coord[i][1] + abs(coord[i][0] - coord[i + 1][0]) + coord[i + 1][1]
    if res > dist or res == -1:
        res = dist

print(res)
