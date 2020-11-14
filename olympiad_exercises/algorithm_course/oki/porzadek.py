def prefix_maker(_pref_n, _pref_r, _pref_pair, _flow):
    for _i in range(1, len(flow)):
        if _flow[_i] == 'N':
            _pref_n.append(pref_n[_i - 1] + 1)
            _pref_r.append(pref_r[_i - 1])
            _pref_pair.append(_pref_r[_i] + pref_pair[_i - 1])
        elif _flow[_i] == 'R':
            _pref_n.append(pref_n[_i - 1])
            _pref_r.append(pref_r[_i - 1] + 1)
            _pref_pair.append(pref_pair[_i - 1])


def count_ratio_of_mess(_quest, _pref_n, _pref_r, _pref_pair):
    _res = _pref_pair[_quest[1]] - _pref_pair[_quest[0] - 1]
    _res -= _pref_r[_quest[0] - 1] * (_pref_n[_quest[1]] - _pref_n[_quest[0] - 1])
    if _res < 0:
        _res = 0
    return _res


f_len = int(input())
flow = list(map(str, input()))
flow.insert(0, '0')
q_len = int(input())

pref_n = [0]
pref_r = [0]
pref_pair = [0]

prefix_maker(pref_n, pref_r, pref_pair, flow)

results = []
for i in range(q_len):
    quest = list(map(int, input().split()))
    results.append(count_ratio_of_mess(quest, pref_n, pref_r, pref_pair))

for i in range(len(results)):
    print(results[i])
