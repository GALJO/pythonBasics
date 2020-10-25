input_numb = input().split()
k = int(input())

counter = 0
_sum = int(input_numb[0])
j = 0
n = len(input_numb)
for i in range(n):
    while (j < (n - 1)) and (_sum < k):
        j += 1
        _sum += int(input_numb[j])
    if _sum == k:
        counter += 1
    _sum -= int(input_numb[i])

print(counter)
