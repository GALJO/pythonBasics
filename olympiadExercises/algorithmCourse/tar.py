z = int(input())  # liczba zagadek
results = []


def find_result(_p, _q):
    center = 0
    start = 1
    end = q
    done = False
    while not done:
        center = int((start + end) / 2)
        res = (center * center * center) + (_p * center)
        if res == _q:
            done = True
        elif start > end:
            return "NIE"
        elif res > _q:
            end = center - 1
        elif res < _q:
            start = center + 1
    return center


for i in range(z):
    pq = input().split()  # liczby podane do równania \/
    p = int(pq[0])
    q = int(pq[1])
    results.append(str(find_result(p, q)))

for x in range(len(results)):
    print(results[x])