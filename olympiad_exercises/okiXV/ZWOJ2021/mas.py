def is_descending(_value):
    if _value == 'M':
        return True
    else:
        return False


nq = input().split()
n = int(nq[0])
q = int(nq[1])
A = list(map(int, input().split()))
O = []
for i in range(q):
    O.append(input().split())

for i in range(q):
    actual_op = O[i]
    A[int(actual_op[0]) - 1:int(actual_op[1])] = sorted(A[int(actual_op[0]) - 1:int(actual_op[1])],
                                                            reverse=is_descending(actual_op[2]))

for el in A:
    print(el, end=' ')
