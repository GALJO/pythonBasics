def read_dict_info():
    _inp = open(file='../logs/slo_inp.txt', mode='r')
    _n = int(_inp.readline())
    _dict = {}
    for _i in range(_n):
        _act_line = _inp.readline().split('#')
        _act_line[1] = _act_line[1][:-1]
        _dict.setdefault(_act_line[0], ' ')
        _dict[_act_line[0]] = _act_line[1]
    return _n, _dict


def binary_search(_tab, _str):
    start = 0
    end = len(_tab) - 1
    while start < end:
        center = (start + end + 1) // 2
        if _tab[center] <= _str:
            start = center
        else:
            end = center - 1
    return start


def main():
    _finds = []
    _keys = sorted(list(dict_.keys()))
    for _i in range(quest_amount):
        _act_quest = quests[_i]
        _key_ndx = binary_search(_keys, _act_quest)
        if _keys[_key_ndx] != _act_quest:
            _finds.append('-')
        else:
            _finds.append(dict_[_keys[binary_search(_keys, _act_quest)]])
    return _finds


n, dict_ = read_dict_info()
quest_amount = int(input())
quests = input().split()
results = main()
for res in results:
    print(res)
