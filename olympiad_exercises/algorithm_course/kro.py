import lib

amount_of_obstacles = int(input())
results = []

for i in range(amount_of_obstacles):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    results.append(lib.power(a + 1, b) % 10000)

for i in range(len(results)):
    print(int(results[i]))
