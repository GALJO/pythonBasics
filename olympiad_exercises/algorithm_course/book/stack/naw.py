n = int(input())
for i in range(n):
    actual_series = list(map(str, input()))
    stack = []
    for j in range(len(actual_series)):
        if actual_series[j] == '(' or actual_series[j] == '[' or actual_series[j] == '{':
            stack.append(actual_series[j])
            continue

        if actual_series[j] == ')':
            if stack[-1] == '(':
                stack.pop()
        elif actual_series[j] == ']':
            if stack[-1] == '[':
                stack.pop()
        elif actual_series[j] == '}':
            if stack[-1] == '{':
                stack.pop()

    if len(stack) == 0:
        print('TAK')
    else:
        print('NIE')
