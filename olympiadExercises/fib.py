number = int(input()) - 1

fib = [1, 1]
for i in range(1, number):
    fib.append(fib[i - 1] + fib[i])

print(fib[-1])
