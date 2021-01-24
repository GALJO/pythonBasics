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


def main():
    _results = []
    for _i in range(quest_amount):
        dict_.setdefault(quests[_i], '-')
        _results.append(dict_[quests[_i]])
    return _results


n, dict_ = read_dict_info()
quest_amount = int(input())
quests = input().split()
results = main()
for res in results:
    print(res)
