def is_number_even_digit(_number):
    _sum = 0
    for _i in range(len(str(_number))):
        if int(str(_number)[_i]) % 2 == 0:
            continue
        else:
            return False
    return True


def main():
    _amount_of_even_digit_numbers = 0
    _actual_number = 1
    _actual_even_digit_number = -1
    while n > _amount_of_even_digit_numbers:
        if is_number_even_digit(_actual_number):
            _actual_even_digit_number = _actual_number
            _amount_of_even_digit_numbers += 1
        _actual_number += 1
    return _actual_even_digit_number


n = int(input())
print(main())