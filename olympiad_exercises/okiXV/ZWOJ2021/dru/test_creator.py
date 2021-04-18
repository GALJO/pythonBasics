from random import randint, choice
from string import ascii_lowercase

n = randint(1, 10)
print(n)

ascii_ = ascii_lowercase
for i in range(n):
    str_len = randint(1, 10)
    str_ = ''
    for j in range(str_len):
        str_ += choice(ascii_)
    print(str_)

