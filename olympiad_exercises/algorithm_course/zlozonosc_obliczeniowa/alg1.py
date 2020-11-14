input_numb = input().split()
k = int(input())

counter = 0

for i in range(len(input_numb)):
    for j in range(i, len(input_numb)):
        _sum = 0
        for s in range(i, j + 1):
            _sum += int(input_numb[s])
        if _sum == k:
            counter += 1

print(counter)
