ile = 0
for liczba in range(1, 161):
    if liczba % 2 == 0:
        ile += 1
    elif liczba % 3 == 0:
        ile += 1
    elif liczba % 5 == 0:
        ile += 1
print(ile)
