length = int(input())
series = input().split()
characters = input().split()
characters = {
    'a': int(characters[0]) - 1,
    'j': int(characters[1]) - 1
}

sum_ = 0
for i in range(characters['a'], len(series) + 1, characters['j']):
    sum_ += int(i)

average = sum_ / length
print(int(average))
