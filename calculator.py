import datetime


def print_result(numb1, numb2, result, op):
    print(str(numb1) + " " + op + " " + str(numb2) + " = " + str(result))


def finish_app():
    if operation[0] == "s":
        return True
    return False


def is_number1_float(_one):
    try:
        float(_one)
    except ValueError:
        return False
    return True


def is_number2_float(_two):
    try:
        float(_two)
    except ValueError:
        return False
    return True


def symb_valid(_symb):
    if _symb == "+":
        return True
    if _symb == "-":
        return True
    if _symb == "*":
        return True
    if _symb == "/":
        return True
    return False


def calculate(_one, _two, _symb):
    result = None
    if _symb == "+":
        result = _one + _two
    if _symb == "-":
        result = _one - _two
    if _symb == "*":
        result = _one * _two
    if _symb == "/":
        result = _one / _two
    return result


print("Witaj w moim kalkulatorze w języku Python!")

while True:
    print(" ")
    print("Wprowadź działanie (np. 5 + 7 lub 4 * 8, s aby zakończyć)")
    operation = input()
    operation = operation.split()
    one = operation[0]

    if finish_app():
        print(" ")
        print("Dziękuję za korzystanie z kalkulatora!")
        exit(0)

    two = operation[2]
    symb = str(operation[1])

    if not is_number1_float(one) or not is_number2_float(two):
        print("Podałeś niepoprawną liczbę.")
        continue

    if not symb_valid(symb):
        print("Podałeś niepoprawny symbol.")
        continue

    one = float(one)
    two = float(two)

    result = "{} {} {} = {}".format(one, symb, two, calculate(one, two, symb))
    print(result)
    log = open("logs/calculator_log.txt", "a+")
    log.write("[{}] Działanie: {}\n".format(datetime.datetime.now(), result))
    log.close()
