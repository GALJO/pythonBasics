def find_fraction(_desc):
    _res = {'p': 0, 'q': 0}
    for _i in range(len(_desc)):
        if _desc[_i] == 'G':
            _res['p'] += 1
        elif _desc[_i] == 'P':
            _res['q'] += 1
    return _res


def count_


def main():
    _fraction = find_fraction(zigzag_desc)

    return '{}/{}'.format(_fraction['p'], _fraction['q'])


zigzag_desc = input()
print(main())
