# @return index near searching _num
def binary_search(_tab, _num):
    start = 0
    end = len(_tab) - 1
    while start < end:
        center = (start + end + 1) // 2
        if int(_tab[center]) <= _num:
            start = center
        else:
            end = center - 1
    return start


def find_or_get_left(_tab, _num):
    index = binary_search(_tab, _num)
    if int(_tab[index]) > _num:
        return index - 1
    return index


def read_integers(_f):
    return list(map(int, _f.readline().replace('\n', '').split()))


inp = open('haybales.in', 'r', encoding='utf-8')
out = open('haybales.out', 'w', encoding='utf-8')
nq = read_integers(inp)
n = nq[0]
q = nq[1]
haybales = sorted(read_integers(inp))

for i in range(q):
    quest = read_integers(inp)
    i1 = find_or_get_left(haybales, quest[0] - 1)
    i2 = find_or_get_left(haybales, quest[1])
    out.write(str(i2 - i1) + '\n')
