def print_result(numb1, numb2, result, op):
    print(str(numb1) + " " + op + " " + str(numb2) + " = " + str(result))


def finish_app():
    if numbers == "s":
        return True
    return False


def is_number1_float():
    try:
        float(one)
    except ValueError:
        return False
    return True


def is_number2_float():
    try:
        float(two)
    except ValueError:
        return False
    return True


def len_valid():
    if int(len(numbers)) >= 5:
        return True
    return False


def symb_valid():
    if symb == "+":
        return True
    if symb == "-":
        return True
    if symb == "*":
        return True
    if symb == "/":
        return True
    return False


def calculate():
    result = None
    if symb == "+":
        result = one + two
    if symb == "-":
        result = one - two
    if symb == "*":
        result = one * two
    if symb == "/":
        result = one / two
    return result


print("Witaj w moim kalkulatorze w języku Python!")

while True:
    print(" ")
    print("Wprowadź działanie (możesz dodawać: '+' odejmować: '-' mnożyć: '*' dzielić: '/'  lub wyjść: 's'):")

    numbers = input()
    if finish_app():
        print(" ")
        print("Dziękuję za korzystanie z kalkulatora!")
        exit(0)

    if not len_valid():
        print("Za mało argumentów!")
        continue

    one = numbers[0]
    symb = str(numbers[2])
    two = numbers[4]

    if not is_number1_float():
        print("Niepoprawny pierwszy argument!")
        continue
    if not is_number2_float():
        print("Niepoprawny drugi argument!")
        continue
    if not symb_valid():
        print("Podałeś niepoprawny symbol!")
        continue

    one = float(one)
    two = float(two)

    print("{} {} {} = {}".format(one, symb, two, calculate()))
