nk = input().split()
n, k = int(nk[0]), int(nk[1])
w = list(map(int, input().split()))
w.sort()

amount_of_speeches = {w[0]: 1}
for i in range(1, n - k + 1):
    amount_of_speeches.setdefault(w[i], 0)
    amount_of_speeches[w[i]] += 1

print(max(list(amount_of_speeches.values())) + k)