n = int(input())
s = input().split()

counter = 0

for i in range(n):
    if int(s[i]) == 0:
        for x in range(i, len(s)):
            if int(s[x]) == 1:
                counter += 1

print(counter)
