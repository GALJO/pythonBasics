def binary_search(_p, _q):
    start = 0
    end = 10000000
    while start < end:
        _x = (start + end) // 2
        _res = _x ** 3 + _p * _x
        if _res < _q:
            start = _x + 1
        else:
            end = _x
    return start


def main():
    for quest in quests:
        _x = binary_search(quest[0], quest[1])
        _res = _x ** 3 + quest[0] * _x
        if _res == quest[1]:
            print(_x)
        else:
            print('NIE')


z = int(input())
quests = []

for i in range(z):
    quests.append(tuple(map(int, input().split())))

main()
