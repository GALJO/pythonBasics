import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


ws = input().split()
w = int(ws[0])
s = int(ws[1])
d = get_ints()

length = 1
result = -1
amount = int(d[0])
j = 0

for i in range(0, w):
    while (j < w - 1) and (amount < s) and (length < result or result == -1):
        j += 1
        amount += d[j]
        length += 1

    if amount == s:
        if length < result or result == -1:
            result = length
            if result == 1:
                break

    amount -= d[i]
    length -= 1

if result == -1:
    print('N')
else:
    print(result)
