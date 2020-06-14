def input_number(message):
    print(message)
    return float(input())


def print_result(numb1, numb2, result, op):
    print(str(numb1) + " " + op + " " + str(numb2) + " = " + str(result))


print("Witaj w moim pierwszym kalkulatorze w języku Python!")
print(" ")

one = input_number("Podaj pierwszą liczbę")
two = input_number("Podaj drugą liczbę")

addition = one + two
subtraction = one - two
multiplication = one * two
division = one / two

print("Twój wynik to:")
print_result(one, two, addition, "+")
print_result(one, two, subtraction, "-")
print_result(one, two, multiplication, "*")
print_result(one, two, division, "/")
