def second():
    print('x', end='')
    for i in range(5, 17, 4):
        print('xx', end='')
    print('xxx')


def third(t):
    maxi = 0
    for i in range(5):
        if t[i] > maxi:
            print('poprawiam')
            maxi = t[i]


def fourth(p):
    s = 'napisik'
    t = ''
    for i in range(len(p)):
        t = t + s[p[i]]
    print(t)


def tenth(numb):
    while numb > 0:
        if (numb > 5) and (numb < 95):
            numb -= 10
        numb = max(0, numb)
        numb = min(100, numb)


def twelfth(numbs):
    res = []
    amount = {}
    for x in numbs:
        if x not in amount:
            amount[x] = 0
        amount[x] += 1
    for el in sorted(amount.items()):
        for i in range(el[1]):
            res.append(el[0])
    return res


def thirteenth(n):
    if n == 10:
        return n
    return 1 + thirteenth(n + 2)


def nineteenth(numb):
    counter = 2
    for i in range(2, (numb // 2) + 1):
        if numb % i == 0:
            counter += 1
    print(counter)


def twentieth():
    amount = 0
    for i in range(1, 254):
        if twentieth2(i):
            amount += 1
    print(amount)


def twentieth2(n):
    if n == 0:
        return False
    return (n % 10 == 1) or (twentieth2(n // 10))


def twenty_second():
    elements = [(3, 2), (2, 5), (2, 9), (1, 7), (9, 0)]
    elements.sort()
    print(elements[2][0], elements[2][1])


def twenty_third(numb):
    if numb == 0:
        return 1
    return twenty_third(numb // 2) + numb % 2


def twenty_fifth():
    amount = 0
    numbs = [5, 3, 2, 9, 5, 2, 9, 3, 1, 7]
    for i in range(len(numbs)):
        for j in range(i + 1, len(numbs)):
            if (numbs[i] + numbs[j]) % 2 == 0:
                amount += 1
    print(amount)


def twenty_seventh(numb):
    if numb == 1:
        return 0
    return 1 + twenty_seventh(numb // 2)


def twenty_ninth():
    amount = 0
    numbs = [4, 9, 8, 5, 3, 9, 3, 0, 10, 3]
    for i in range(len(numbs)):
        for j in range(i + 1, len(numbs)):
            if (numbs[i] + numbs[j]) >= 10:
                amount += 1
    print(amount)



