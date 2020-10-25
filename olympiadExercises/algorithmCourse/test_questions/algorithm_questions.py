def first_and_second(x, y):
    if x == 0:
        return y
    return first_and_second(x // 10, 10 * y + (x % 10))


def third(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            temp = t[i]
            t.remove(i)
            t.insert(i, t[i + 1])
    return t


print(third([2, 5, 6]))
