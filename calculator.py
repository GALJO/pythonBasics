print("Witaj w moim pierwszym kalkulatorze w języku Python!")
print(" ")
print("Podaj pierwszą liczbę:")
one = float(input())
print("Podaj drugą liczbę:")
two = float(input())

addition = one + two
subtraction = one - two
multiplication = one * two
division = one / two

print("Twój wynik to:")
print(str(one) + " + " + str(two) + " = " + str(addition))
print(str(one) + " - " + str(two) + " = " + str(subtraction))
print(str(one) + " * " + str(two) + " = " + str(multiplication))
print(str(one) + " / " + str(two) + " = " + str(division))

