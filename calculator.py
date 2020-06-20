def print_result(numb1, numb2, result, op):
    print(str(numb1) + " " + op + " " + str(numb2) + " = " + str(result))


def finish_app():
    if one == "s":
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
    print("Wprowadź argumenty:")
    print("Pierwsza liczba (aby wyjść 's'):")
    one = input()

    if finish_app():
        print(" ")
        print("Dziękuję za korzystanie z kalkulatora!")
        exit(0)
    if not is_number1_float():
        print("Podałeś niepoprawną liczbę.")
        continue

    print("Znak matematyczny (+, -, * lub /)")
    symb = input()
    if not symb_valid():
        print("Podałeś niepoprawny symbol.")
        continue

    print("Druga liczba:")
    two = input()
    if not is_number2_float():
        print("Podałeś niepoprawną liczbę.")
        continue

    one = float(one)
    two = float(two)

    print("{} {} {} = {}".format(one, symb, two, calculate()))
