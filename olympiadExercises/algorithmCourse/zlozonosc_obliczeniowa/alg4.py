input_numb = input().split()
k = int(input())

prefix_sum = []
counter = 0
_sum = input_numb[0]
j = 0

prefix_sum.append(0)
prefix_sum.append(int(input_numb[0]))
for i in range(len(input_numb) - 1):
    prefix_sum.append(int(input_numb[i]) + int(input_numb[i + 1]))

print(prefix_sum)
