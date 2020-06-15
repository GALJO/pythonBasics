def list_finish(a_position):
    if a_position == "k":
        return 3
    else:
        return 0


def k_remove_safely(a_shop_list=[]):
    try:
        a_shop_list.remove("k")
    except:
        return 0


def write_list():
    print(" ")
    print("Twoja nowa lista to:")
    for i in range(len(shop_list)):
        print(str(i + 1) + "." + " " + shop_list[i])


def fill_list(a_shop_list):
    while True:
        el = input()
        if el == "k":
            return
        a_shop_list.append(el)


def valid_del(a_rmv):
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


def valid_choice(a_choice):
    if a_choice == "list":
        print("Możesz:")
        print("'dodaj' - dodać nowy punkt")
        print("'usuń' - usunąć punkt")
        print("'zalicz' - dodaj tick do punktu i przenieś go na dół")
        print("'wróć' - wróć poprzednią operację")
        print("'reset' - zresetuj wszystko - wróć do początku programu")

    if a_choice == "dodaj":
        print(" ")
        print("Wpisz punkt do dodania:")
        shop_list.append(str(input()))

    if a_choice == "usuń":
        print(" ")
        print("Wpisz numer punktu, który chcesz usunąć:")
        rmv = input()
        valid_del(rmv)


print("Zrób zakupy z Python Shopping 1.0!")
print(" ")

print("Utwórz listę zakupów: (każdy enter to nowa pozycja, aby zakończyć 'k')")
shop_list = []
fill_list(shop_list)

while True:
    write_list()
    print(" ")
    print("Jaką chcesz wykonać akcję na liście? (list - lista możliwych opcji)")
    choice = str(input())
    valid_choice(choice)


