def test(_width, _tab, _center, _others_len):
    for j in range(i, i + _width):
        if j == _center:
            if _tab[j] < _width:
                return False
        else:
            if _tab[j] < _others_len:
                return False
    return True


n = int(input())
T = tuple(map(int, input().split()))

max_res = 0
for i in range(n):
    max_l = (n - i - 1) // 2
    if max_l <= max_res:
        break
    for L in range(max_l, max_res, -1):
        width = 2 * L + 1
        others_len = L + 1
        center_ndx = i + L
        if test(width, T, center_ndx, others_len):
            max_res = L
            break

print(max_res)
