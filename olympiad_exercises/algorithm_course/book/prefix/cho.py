nm = input().split()
n, m = int(nm[0]), int(nm[1])
c = list(map(int, input().split()))

results = []
for i in range(m):
    actual_quest = tuple(map(int, input().split()))
    results.append(min(c[actual_quest[0] - 1:actual_quest[1]]))

for res in results:
    print(res)