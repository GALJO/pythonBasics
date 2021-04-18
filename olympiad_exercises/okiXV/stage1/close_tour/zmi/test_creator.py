from random import randint, choice
from string import ascii_lowercase

ascii_ = ascii_lowercase
str_len = randint(1, 1000)
str_ = ''
for j in range(str_len):
    str_ += choice(ascii_)
print(str_)

