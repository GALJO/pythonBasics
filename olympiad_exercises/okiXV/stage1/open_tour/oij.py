# https://szkopul.edu.pl/problemset/problem/WawC7bmwUyPKAG25CCKdFiCP/site/?key=submissions - 100% points

inp = list(map(str, input()))

count = 0
o = False
i = False
j = False

for x in range(len(inp)):
    if inp[x] == 'o':
        o = True
    elif inp[x] == 'i' and o is True:
        i = True
    elif inp[x] == 'j' and i is True:
        j = True
    if o is True and i is True and j is True:
        count += 1
        o = False
        i = False
        j = False

if count == 0:
    print('NIE')
else:
    print(count)
