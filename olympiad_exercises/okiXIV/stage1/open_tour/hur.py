def main():
    for _i in range(1, n + 1):
        if _i % 11 == 0 and _i % 7 == 0:
            print('Wiwat!')
            continue
        if _i % 7 == 0:
            print('Hurra!')
            continue
        if _i % 11 == 0:
            print('Super!')
            continue
        if _i % 7 != 0 and _i % 11 != 0:
            print(_i)


n = int(input())
main()
