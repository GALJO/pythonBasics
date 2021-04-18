def prefix_sum(_tab):
    _pref = [0]
    for _i in range(0, len(_tab)):
        _pref.append(_pref[_i] + _tab[-(_i + 1)])
    return _pref


n = int(input())
s = list(map(int, input().split()))

prefix = list(reversed(prefix_sum(s)))

res = 0
for i in range(n):
    if s[i] == 0:
        res += prefix[i + 1]

print(res)