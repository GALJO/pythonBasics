inp = input().split()
h = int(inp[0])
m = int(inp[1])
s = int(inp[2]) + 1

if s / 60 >= 1:
    m += int(s / 60)
    s -= (int((s / 60)) * 60)

if m / 60 >= 1:
    h += int(m / 60)
    m -= (int(m / 60) * 60)

if h / 24 >= 1:
    h = h % 24

print('{:02d}:{:02d}:{:02d}'.format(h, m, s))
