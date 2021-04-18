from random import randint

n = randint(1, 10)
print(n)

for i in range(n):
    one = randint(1, 10)
    two = randint(one, 10)
    print('{} {}'.format(one, two))
