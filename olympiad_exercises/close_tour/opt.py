n = int(input())
k = sorted(list(map(int, input().split())))
r = list(reversed(sorted(map(int, input().split()))))

result = 0
for i in range(len(k)):
    result += int(str(k[i]) + str(r[i]))

print(result)