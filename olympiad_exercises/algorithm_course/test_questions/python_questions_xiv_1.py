def fifteenth():
    counter = 0
    for i in range(ord('a'), ord('z')):
        print('X')
        counter += 1
    print('\n' + str(counter))


def sixteenth(x):
    return x * x + 2 * x + 3


def seventeenth(x):
    if x == 3:
        return x * x
    return seventeenth(x + 1)


def fiftieth():
    a = 0
    while a < 1000:
        print('X')
        a += 1
        continue


def fifty_fourth():
    res = 0
    if 17 % 5 == 2:
        res += 1
    if 10 % 3 == 2:
        res -= 1
    print(res)


def seventieth():
    if -0 < 0:
        print('TAK')
    else:
        print('NIE')
