input_numb = input().split()
k = int(input())

counter = 0

for i in range(len(input_numb)):
    _sum = 0
    for j in range(i, len(input_numb)):
        _sum += int(input_numb[j])
        if _sum == k:
            counter += 1

print(counter)
