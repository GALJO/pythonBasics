n = int(input())
T = tuple(sorted(map(int, input().split())))

st = 0
end = 1
res = 0
while st < n - 2:
    if T[end] - T[st] > 1:
        st += 1
        end = st + 1
    else:
        if end - st == 2:
            res += 1
            st = end + 1
            end = st + 1
        else:
            end += 1

print(res)
