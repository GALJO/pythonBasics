def write_list():
    print(" ")
    print("Twoja nowa lista to:")
    for i in range(len(shop_list)):
        print(str(i + 1) + "." + " " + shop_list[i])


def fill_list(a_shop_list):
    print("Utwórz listę zakupów: (każdy enter to nowa pozycja, aby zakończyć 'k')")
    while True:
        el = input()
        if el == "k":
            save_old_list()
            return
        a_shop_list.append(str(el))


def valid_del(a_rmv):
    if a_rmv == "zal":
        save_old_list()
        for i in range(len(shop_list)):
            point = shop_list[i - 1]
            if point[-1] == "✓":
                shop_list.pop(i - 1)
        return

    try:
        int(a_rmv)
    except:
        print("Niepoprawny numer!")
        return

    if a_rmv == 0:
        shop_list.pop(int(a_rmv))
        return

    if int(a_rmv) > len(shop_list):
        print("Niepoprawny numer!")
        return

    shop_list.pop(int(a_rmv) - 1)


def valid_tick():
    tick_point = input()

    try:
        int(tick_point)
    except:
        print("Nieprawidłowy numer!")
        return

    tick_point = int(tick_point)

    if tick_point == 0:
        tick_point_str = shop_list[tick_point]
        shop_list.pop(tick_point)
        shop_list.append(tick_point_str + " ✓")
        return

    if tick_point > len(shop_list):
        print("Nieprawidłowy numer!")
        return

    tick_point_str = shop_list[tick_point - 1]
    shop_list.pop(tick_point - 1)
    shop_list.append(tick_point_str + " ✓")


def save_old_list():
    old_list.clear()
    for i in range(len(shop_list)):
        old_list.append("x")
        old_list[i] = shop_list[i]


def valid_choice(a_choice):
    if a_choice == "list":
        print("Możesz:")
        print("'dodaj' - dodać nowy punkt")
        print("'usuń' - usunąć punkt (jeśli w pole wpisane 'zal' to usunie wszystkie zaliczone punkty)")
        print("'zalicz' - dodaj tick do punktu i przenieś go na dół")
        print("'wróć' - wróć poprzednią operację")
        print("'reset' - zresetuj wszystko - wróć do początku programu")
        print("'wyjdź' - wyłącz aplikację")
        # TODO do ogarnięcia "usuń wykonane" (usuwanie tych, które na poz -1 mają ticka)
        return

    if a_choice == "dodaj":
        save_old_list()
        print(" ")
        print("Wpisz punkt do dodania:")
        shop_list.append(str(input()))
        return

    if a_choice == "usuń":
        save_old_list()
        print(" ")
        print("Wpisz numer punktu, który chcesz usunąć:")
        rmv = input()
        valid_del(rmv)
        return

    if a_choice == "zalicz":
        save_old_list()
        print(" ")
        print("Wpisz numer punktu, który chcesz zaliczyć:")
        valid_tick()
        return

    if a_choice == "reset":
        print(" ")
        print("Czy na pewno chcesz zresetować listę? Poskutkuje to straceniem WSZYSTKICH DANYCH i uruchomi ponownie "
              "aplikację. Potwierdź (T) badź anuluj (N)")
        sure = str(input())
        if sure == "T" or sure == "t":
            print("|PROCESS CLOSED|")
            print("|PROCESS STARTED|")
            print("_______________________")
            shop_list.clear()
            old_list.clear()
            fill_list(shop_list)
            return
        else:
            print("Anulowano")
            return

    if a_choice == "wyjdź":
        print(" ")
        print("Czy na pewno chcesz wyłączyć aplikację? Poskutkuje to straceniem WSZYSTKICH DANYCH. Wyjdź (T) badź "
              "anuluj (N)")
        sure = str(input())
        if sure == "T" or sure == "t":
            print("|PROCESS CLOSED|")
            print("_______________________")
            exit(0)
        else:
            print("Anulowano")
            return

    if a_choice == "wróć":
        shop_list.clear()
        for i in range(len(old_list)):
            shop_list.append("x")
            shop_list[i] = old_list[i]
        print("Przywrócono do stanu sprzed ostatniej operacji.")
        return


print("|PROCESS STARTED|")
print("_______________________")
print("Zrób zakupy z Python Shopping 1.0!")
print(" ")

shop_list = []
old_list = []
fill_list(shop_list)

while True:
    write_list()
    print(" ")
    print("Jaką chcesz wykonać akcję na liście? (list - lista możliwych opcji)")
    choice = str(input())
    valid_choice(choice)
