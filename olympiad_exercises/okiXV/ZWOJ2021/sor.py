def main():
    sorted_a = sorted(A)
    sorted_a.sort(key=len)
    return sorted_a


n = int(input())
A = []
for i in range(n):
    A.append(input())

res = main()
for el in res:
    print(el)
