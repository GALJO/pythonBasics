mark_number = int(input())
marks = input().split()

l_marks = {
    'one': 0,
    'two': 0,
    'three': 0,
    'four': 0,
    'five': 0,
    'six': 0,
}

for i in range(len(marks)):
    if int(marks[i]) == 1:
        l_marks['one'] += 1
    elif int(marks[i]) == 2:
        l_marks['two'] += 1
    elif int(marks[i]) == 3:
        l_marks['three'] += 1
    elif int(marks[i]) == 4:
        l_marks['four'] += 1
    elif int(marks[i]) == 5:
        l_marks['five'] += 1

l_marks['six'] = mark_number - l_marks['one'] - l_marks['two'] - l_marks['three'] - l_marks['four'] - l_marks['five']

print(l_marks['one'], end=' ')
print(l_marks['two'], end=' ')
print(l_marks['three'], end=' ')
print(l_marks['four'], end=' ')
print(l_marks['five'], end=' ')
print(l_marks['six'], end=' ')
