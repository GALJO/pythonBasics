from math import ceil

n = int(input())
a = list(map(int, input().split()))

res = 0
for i in range(1, n):
    first_part = sorted(a[:i])
    second_part = sorted(a[i:])
    if (
            first_part[0] == second_part[0] or
            first_part[0] == second_part[-1] or
            first_part[-1] == second_part[0] or
            first_part[-1] == second_part[-1]
    ) and (first_part[ceil(len(first_part) / 2) - 1] == second_part[ceil(len(second_part) / 2) - 1]):
        res += 1

print(res)
