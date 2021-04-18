def last_button(_values):
    _biggest = max(_values)
    return [_biggest] * len(_values)


nm = input().split()
n, m = int(nm[0]), int(nm[1])
p = list(map(int, input().split()))

values = [0] * n
for i in range(m):
    if p[i] == n + 1:
        values = last_button(values)
    else:
        values[p[i] - 1] += 1

print(values)
