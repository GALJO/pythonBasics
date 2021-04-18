n = int(input())
a = list(map(int, input().split()))
k = list(map(int, input().split()))

size_stack = [a[0]]
direction_stack = [k[0]]
for i in range(1, n):
    if direction_stack[-1] == 1 and k[i] == 0:
        if size_stack[-1] < a[i]:
            size_stack.pop()
            direction_stack.pop()
            direction_stack.append(k[i])
            size_stack.append(a[i])
    else:
        direction_stack.append(k[i])
        size_stack.append(a[i])

print(len(size_stack))



