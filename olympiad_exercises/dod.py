numbers = input().split()


def sum_of_numbers(start, count):
    _sum = 0
    for i in range(count):
        _sum += start + i
    return _sum


def print_numbers(start, count):
    for i in range(count):
        print(start + i, end=' ')


in_amount = int(numbers[0])
in_sum = int(numbers[1])

number = int(in_sum / in_amount)
while True:
    _sum = sum_of_numbers(number, in_amount)
    if _sum == in_sum:
        print_numbers(number, in_amount)
        break
    elif _sum < in_sum:
        print('NIE')
        break
    number -= 1
