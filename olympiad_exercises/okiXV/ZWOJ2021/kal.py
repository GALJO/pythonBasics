def fill_list_with_ints(_len):
    _list = list(map(int, input().split()))
    return _list


def write_quests(_amount):
    _list = []
    for _i in range(_amount):
        _inp = input().split()
        _list.append((int(_inp[0]), int(_inp[1]), _inp[2]))
    return _list


def convert_date(_quest, _months_1, _months_2):
    _am_of_days = _quest[0]
    for _i in range(_quest[1] - 1):
        _am_of_days += _months_1[_i]
    _2_month = 1
    _2_day = 0
    for _i in range(len(_months_2)):
        if _am_of_days > _months_2[_i]:
            _am_of_days -= _months_2[_i]
            _2_month += 1
        else:
            _2_day = _am_of_days
            break
    return '{} {}'.format(_2_day, _2_month)


def main():
    _results = []
    for _i in range(z):
        _act_quest = quests[_i]
        if _act_quest[2] == 'A':
            _results.append(convert_date(_act_quest, a_months, b_months))
        else:
            _results.append(convert_date(_act_quest, b_months, a_months))
    return _results


nm = input().split()
n = int(nm[0])
m = int(nm[1])
a_months = fill_list_with_ints(n)
b_months = fill_list_with_ints(m)
z = int(input())
quests = write_quests(z)

results = main()

for el in results:
    print(el)
