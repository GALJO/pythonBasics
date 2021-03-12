from sys import stdin

n = int(stdin.readline())
P = sorted(tuple(map(int, stdin.readline().split())))

P[0] = P[0] - 1
for i in range(1, n):
    if P[i] - P[i - 1] == 1:
        continue
    elif P[i] - P[i - 1] > 1:
        P[i] -= 1
    elif P[i] - P[i - 1] < 1:
        P[i] += 1

print(len(set(P)))
