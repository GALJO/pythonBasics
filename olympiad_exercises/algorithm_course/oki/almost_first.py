def sieve(_numb):
    first_dividers = []
    for i in range(_numb + 1):
        first_dividers.append(0)
    first_dividers[0] = 1
    first_dividers[1] = 1
    for j in range(2, _numb + 1):
        if first_dividers[j] != 0:
            continue
        if first_dividers[j] == 0:
            first_dividers[j] = j
            for x in range(j * 2, _numb + 1, j):
                if first_dividers[x] == 0:
                    first_dividers[x] = j
    return first_dividers


n = int(input())

counter = 0
dividers = sieve(n)
for i in range(6, n + 1):
    alm_first = True
    first_divider = dividers[i]
    sec_divider = 0
    numb = i
    while True:
        numb = numb // dividers[numb]
        divider = dividers[numb]
        if numb <= 1:
            break
        if divider != first_divider and sec_divider == 0:
            sec_divider = divider
        if divider != sec_divider and sec_divider != 0:
            alm_first = False
            break
    if sec_divider == 0 or alm_first is False:
        continue
    else:
        counter += 1

print(counter)
