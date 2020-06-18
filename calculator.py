# TODO refactor and update calculator


def input_number(message):
    print(message)
    return input()


def print_result(numb1, numb2, result, op):
    print(str(numb1) + " " + op + " " + str(numb2) + " = " + str(result))


def finish_app(numb1):
    if numb1 == "s":
        print(" ")
        print("Dziękuję za korzystanie z kalkulatora!")
        exit(0)


def is_number1_float(numb1):
    try:
        float(numb1)
    except ValueError:
        print("Nieprawidłowy pierwszy argument!")
        exit(1)


def is_number2_float(numb2):
    try:
        float(numb2)
    except ValueError:
        print("Nieprawidłowy drugi argument!")
        exit(1)


def validation(numb1, numb2):
    is_number1_float(numb1)
    is_number2_float(numb2)


print("Witaj w moim pierwszym kalkulatorze w języku Python!")

x = 0

while x < 10:
    print(" ")
    one = input_number("Podaj pierwszą liczbę (aby zakończyć 's')")
    finish_app(one)
    two = input_number("Podaj drugą liczbę")

    validation(one, two)

    format_one = float(one[0:])
    format_two = float(two[0:])

    addition = format_one + format_two
    subtraction = format_one - format_two
    multiplication = format_one * format_two
    division = format_one / format_two

    print("Twój wynik to:")
    print_result(one, two, addition, "+")
    print_result(one, two, subtraction, "-")
    print_result(one, two, multiplication, "*")
    print_result(one, two, division, "/")
