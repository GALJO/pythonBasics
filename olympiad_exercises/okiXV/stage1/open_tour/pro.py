# https://szkopul.edu.pl/problemset/problem/iO2JdspPtx_KMGhBTCbLnKYe/site/?key=submissions - 100% points

n = int(input())
programs = sorted(list(map(int, input().split())))
m = int(input())
cds = sorted(list(map(int, input().split())))

if n > m:
    programs = programs[:m]
    n = m

count = 0
cd_start_ndx = 0
for i in range(n):
    for j in range(cd_start_ndx, m):
        is_found = False
        if cds[j] >= programs[i]:
            is_found = True
            count += 1
        cd_start_ndx = cd_start_ndx + 1
        if is_found:
            break

print(count)
