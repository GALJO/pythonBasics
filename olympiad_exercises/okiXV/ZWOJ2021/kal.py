def make_prefixes(_tab):
    _pref = [0]
    for _i in range(0, len(_tab)):
        _pref.append(_pref[_i] + _tab[_i])
    return _pref


def fill_list_with_ints(_len):
    _list = list(map(int, input().split()))
    return _list


def write_quests(_amount):
    _list = []
    for _i in range(_amount):
        _inp = input().split()
        _list.append((int(_inp[0]), int(_inp[1]), _inp[2]))
    return _list


def binary_search(_tab, _x):
    start = 0
    end = len(_tab) - 1
    while start < end:
        cnt = (start + end) // 2
        if _tab[cnt] < _x:
            start = cnt + 1
        else:
            end = cnt
    return start


def days_amount(_prefixes, _quest):
    return _prefixes[_quest[1] - 1] + _quest[0]


def convert_cal(_prefix, _days):
    _month = binary_search(_prefix, _days)
    _day = _days - _prefix[_month - 1]
    return '{} {}'.format(_day, _month)


def main():
    for _i in range(z):
        _act_quest = quests[_i]
        if _act_quest[2] == 'A':
            _days = days_amount(a_months_prefix, _act_quest)
            print(convert_cal(b_months_prefix, _days))
        else:
            _days = days_amount(b_months_prefix, _act_quest)
            print(convert_cal(a_months_prefix, _days))


nm = input().split()
n = int(nm[0])
m = int(nm[1])
a_months = fill_list_with_ints(n)
a_months_prefix = make_prefixes(a_months)
b_months = fill_list_with_ints(m)
b_months_prefix = make_prefixes(b_months)
z = int(input())
quests = write_quests(z)

main()
