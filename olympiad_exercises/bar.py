def is_valid_order(_fruits):
    orange = 0
    apple = 0
    for fruit in _fruits:
        if fruit == 'j':
            apple += 1
        elif fruit == 'p':
            orange += 1
        if apple > orange:
            return False
    return True


def find_correct_stream(_fruits):
    count = 0
    sum = 0
    for x in _fruits:
        if x == "j":
            sum -= 1
        elif x == "p":
            sum += 1
        if sum == -1:
            return _fruits[0:count]
        count += 1
    return _fruits


n = int(input())
fruits = input()
result = 0
next_element = 0

for x in range(n):
    if x < next_element:
        continue

    _a = find_correct_stream(fruits[x:n])
    next_element = x + len(_a)

    if len(_a) <= result:
        continue

    for y in range(0, len(_a)):
        if len(_a) - y <= result:
            break
        if is_valid_order(reversed(_a[0:len(_a) - y])):
            _r = len(_a) - y
            if _r > result:
                result = _r
            break

print(result)
