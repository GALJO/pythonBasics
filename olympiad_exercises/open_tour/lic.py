inp = sorted(list(map(int, input().split())))

if inp[0] == 0 and inp[1] == 0:
    inp.reverse()
elif inp[0] == 0:
    inp[0] = inp[1]
    inp[1] = 0

print('{}{}{}'.format(inp[0], inp[1], inp[2]))
