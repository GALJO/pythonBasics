import lib

def print_list():
    print(" ")
    print("Twoja nowa lista to:")
    for i in range(len(shop_list)):
        print("{}. {}".format(str(i + 1), str(shop_list[i])))


def fill_list(a_shop_list):
    print("Utwórz listę zakupów: (każdy enter to nowa pozycja, aby zakończyć 'k')")
    while True:
        el = input()
        if el == "k":
            save_old_list()
            return None
        a_shop_list.append(str(el))


def remove():
    el = input()

    if el == "zal":
        save_old_list()
        for i in range(len(shop_list)):
            point = shop_list[i - 1]
            if point[-1] == "✓":
                shop_list.pop(i - 1)
        return

    if not lib.is_int(el):
        print("Niepoprawny numer!")
        return None

    el = int(el)

    if el == 0:
        shop_list.pop(el)
        return None

    if el > len(shop_list):
        print("Niepoprawny numer!")
        return None

    shop_list.pop(el - 1)


def tick():
    el = input()

    if not lib.is_int(el):
        print("Niepoprawny numer!")
        return None

    el = int(el)

    if el == 0:
        el_str = shop_list[el]
        shop_list.pop(el)
        shop_list.append(el_str + " ✓")
        return None

    if el > len(shop_list):
        print("Nieprawidłowy numer!")
        return None

    el_str = shop_list[el - 1]
    shop_list.pop(el - 1)
    shop_list.append(el_str + " ✓")


def save_old_list():
    old_list.clear()
    for i in range(len(shop_list)):
        old_list.append("x")
        old_list[i] = shop_list[i]


def sure_system(message):
    print(" ")
    print("{} Potwierdź (T) badź anuluj (N)".format(message))
    ans = str(input())
    if ans == "T" or ans == "t":
        return True
    else:
        return False


def choice():
    ans = str(input())
    if ans == "list":
        print("Możesz:")
        print("'dodaj' - dodać nowy punkt")
        print("'usuń' - usunąć punkt (jeśli w pole wpisane 'zal' to usunie wszystkie zaliczone punkty)")
        print("'zalicz' - dodaj tick do punktu i przenieś go na dół")
        print("'wróć' - wróć poprzednią operację")
        print("'reset' - zresetuj wszystko - wróć do początku programu")
        print("'wyjdź' - wyłącz aplikację")
        return None

    if ans == "dodaj":
        save_old_list()
        print(" ")
        print("Wpisz punkt do dodania:")
        shop_list.append(str(input()))
        return None

    if ans == "usuń":
        save_old_list()
        print(" ")
        print("Wpisz numer punktu, który chcesz usunąć ('zal' kiedy chcesz usunąć zaliczone):")
        remove()
        return None

    if ans == "zalicz":
        save_old_list()
        print(" ")
        print("Wpisz numer punktu, który chcesz zaliczyć:")
        tick()
        return None

    if ans == "reset":
        ans = sure_system("Czy na pewno chcesz zresetować listę? Poskutkuje to straceniem WSZYSTKICH DANYCH.")
        if ans:
            shop_list.clear()
            old_list.clear()
            print("|PROCESS RESTART|")
            print("_______________________")
            print(" ")
            fill_list(shop_list)
        else:
            print("|PROCESS RESTART CANCELED|")
            print("_______________________")
            print(" ")
            return None

    if ans == "wyjdź":
        ans = sure_system("Czy na pewno chcesz wyłączyć aplikację? Poskutkuje to straceniem WSZYSTKICH DANYCH.")
        if ans:
            print("|PROCESS FINISHED|")
            print("_______________________")
            exit(0)
        else:
            print("|PROCESS FINISH CANCELED|")
            print("_______________________")
            print(" ")
            return None

    if ans == "wróć":
        shop_list.clear()
        for i in range(len(old_list)):
            shop_list.append("x")
            shop_list[i] = old_list[i]
        print("Przywrócono do stanu sprzed ostatniej operacji.")
        return None
    else:
        print("Niepoprawna nazwa akcji.")
        return None


print("|PROCESS STARTED|")
print("_______________________")
print("Zrób zakupy z Python Shopping 1.0!")
print(" ")

shop_list = []
old_list = []
fill_list(shop_list)

while True:
    print_list()
    print(" ")
    print("Jaką chcesz wykonać akcję na liście? (list - lista możliwych opcji)")
    choice()
