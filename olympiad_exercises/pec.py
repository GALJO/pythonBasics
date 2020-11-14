def test_thirteen(numb):
    for x in range(len(numb) - 1):
        if numb[x] + numb[x + 1] == '13':
            return True
    return False


def calc_thirteen(numb):
    result = 0
    for x in range(len(numb)):
        result += int(numb[x])
    if result == 13:
        return True
    return False


n = int(input())
unlucky_counter = 1
if n < 139:
    unlucky_counter = 0
else:
    for i in range(140, (n + 1)):
        i_list = list(str(i))
        if not test_thirteen(i_list):
            continue
        if not calc_thirteen(i_list):
            continue
        unlucky_counter += 1

print(unlucky_counter)
