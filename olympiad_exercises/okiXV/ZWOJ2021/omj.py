def make_prefixes(_tab):
    _pref = [0]
    for _i in range(0, len(_tab)):
        _pref.append(_pref[_i] + _tab[_i])
    return _pref


def main():
    _prefixes = make_prefixes(A)
    for _q in quests:
        print(_prefixes[_q[1]] - _prefixes[_q[0] - 1])


nq = input().split()
n = int(nq[0])
q = int(nq[1])
A = list(map(int, input().split()))
quests = []
for i in range(q):
    quests.append(tuple(map(int, input().split())))

main()
