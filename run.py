import calculator
import pythonShopping

number_of_projects = "2"
projects_names = ["kalkulator", "Python Shopping 1.0"]


def main():
    x = True

    print(" ")
    print(
        "Witam w moim projekcie Python! W tej chwili dostępne są " + number_of_projects + " programy. Lista programów:")

    for i in range(len(projects_names)):
        print("- " + projects_names[i])

    print(" ")
    print("Aby wejść do programu wpisz jego nazwę. Jeżeli chcesz wyjść stąd to wpisz 'stop'")
    ans = str(input())

    if ans == 'stop':
        print(" ")
        print("______________")
        print("Miłego dnia!")
        print("______________")
        print(" ")
        exit(0)

    if ans == projects_names[0]:
        calculator.calc_main()
        return

    if ans == projects_names[1]:
        pythonShopping.main()
        return

    for i in range(len(projects_names)):
        if ans != projects_names[i]:
            x = False
        else:
            x = True
        return

    if not x:
        print(" ")
        print("Podałeś niepoprawną nazwę programu!")
        main()
    return


main()
