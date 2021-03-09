from random import randint

n = randint(1, 10000000)
q = randint(1, 1000)
print('{} {}'.format(n, q))


for i in range(n - 1):
    print(randint(-1000, 1000), end=' ')
print(randint(-1000, 1000))

for i in range(q):
    one = randint(1, n)
    two = randint(one, n)
    print('{} {}'.format(one, two))

