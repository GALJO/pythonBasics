from random import randint


def make_correct_input(_sum, _i, _tab):
    _correct = False
    while not _correct:
        if _sum > days_in_year:
            _rand = randint(0, _i - 1)
            if _tab[_rand] == 1:
                continue

            _n = 10
            while True:
                _rand2 = randint(1, _n)
                _res = _tab[_rand] - _rand2
                if _res >= 1:
                    _tab[_rand] -= _rand2
                    break
                elif _res < 1:


            _sum -= 1
        if _sum < days_in_year:
            _rand = randint(0, _i - 1)
            if _tab[_rand] == 1:
                continue
            _tab[_rand] += 1
            _sum -= 1
        if _sum == days_in_year:
            _correct = True
    return _tab


n, m = randint(1, 10), randint(1, 10)
print('{} {}'.format(n, m))

days_in_year = randint(20, 50)

a = []
a_sum = 0
for i in range(n):
    rand = randint(1, 20)
    a.append(rand)
    a_sum += rand

b = []
b_sum = 0
for i in range(m):
    rand = randint(1, 20)
    b.append(rand)
    b_sum += rand

a = make_correct_input(a_sum, n, a)
b = make_correct_input(b_sum, m, b)

z = randint(1, 10)
print(z)

for i in range(z):
    cal_ = randint(0, 1)
    if cal_ == 0:
        cal_ = 'A'
    else:
        cal_ = 'B'

    if cal_ == 'A':
        month = randint(1, n)
        day = randint(1, a[month - 1])
    else:
        month = randint(1, m)
        day = randint(1, a[month - 1])
    print('{} {}'.format(day, month))
