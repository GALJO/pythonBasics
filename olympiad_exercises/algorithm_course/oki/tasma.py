def count_end(_tab):
    x = _tab[0]
    for j in range(len(_tab) - 1, -1, -1):
        if _tab[j] != x:
            return j
    return 0


def count_start(_tab):
    x = _tab[-1]
    for j in range(0, len(_tab), 1):
        if _tab[j] != x:
            return len(_tab) - j - 1
    return 0


quest_numb = int(input())
results = []

for i in range(quest_numb):
    tape_len = int(input())
    tape = list(map(int, input().split()))

    result_start = count_start(tape)
    result_end = count_end(tape)

    if result_start == 0 and result_end == 0:
        results.append('BRAK')
    elif result_start > result_end:
        results.append(result_start)
    else:
        results.append(result_end)

for i in range(len(results)):
    print(results[i])
