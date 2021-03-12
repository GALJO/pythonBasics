# https://szkopul.edu.pl/problemset/problem/gfylBgxHvl-DByutdYjcr7dS/site/?key=statement - 100% points

word = list(map(str, input()))
count = 0
if len(word) == 1:
    count += 0
else:
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count += 1

print(count)
