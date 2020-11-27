a, b, c = input().split()
list = [a, b, c]

if int(a) <= int(9) and int(b) <= 9 and int(c) <= 9 and int(a) > 0 and int(b) > 0 and int(c) > 0:
    list.sort()
    print(list[0] + list[1] + list[2])
elif int(a) == 0 or int(b) == 0 or int(c) == 0:
    list.sort()
    print(list[1] + list[0] + list[2])
