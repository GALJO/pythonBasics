def des(_rain_in_cities, _quests):
    for _quest in _quests:
        if _quest in _rain_in_cities:
            print(_rain_in_cities[_quest])
        else:
            print(0)


nkq = input().split()
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])

cities = {}
for i in range(n):
    day = tuple(map(int, input().split()))
    amount = day[2]
    for _i in range(day[0], day[1] + 1):
        cities.setdefault(_i, 0)
        cities[_i] += amount

quests = []
for i in range(q):
    quests.append(int(input()))

des(cities, quests)
