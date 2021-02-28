import lib

_min = int(input())
_max = int(input())
amount = int(input())

numb = lib.random_number(_min, _max, amount)

f = open("logs/rand_log.txt", 'w+')
for i in range(len(numb)):
    print(numb[i], end='')
    number = str(numb[i]) + '\n'
    f.write(number)

f.close()
print(' ')
print('To copy visit rand_log.txt')