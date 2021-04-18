xys = input().split()
x = int(xys[0])
y = int(xys[1])
z = int(xys[2])

moves = 0
for i in range(x, y + 1, z):
    moves += 1

print(moves)