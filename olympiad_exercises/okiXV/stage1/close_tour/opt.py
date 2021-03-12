# https://szkopul.edu.pl/problemset/problem/XJGk8X4KSGw8yuy5EYEy4rSK/site/?key=statement - 100% points

def main():
    """
    Oblicza sume zoptymalizowych kwot mandatow. Aby kwota byla najmniejsza sklejam:
    - predkosci posortowane rosnaco,
    - numery sluzbowe posortowane malejaco.
    :return: najmniejsza mozliwa suma mandatow
    """
    _result = 0
    for i in range(len(k)):
        _result += int(str(k[i]) + str(r[i]))
    return _result


n = int(input())
k = sorted(list(map(int, input().split())))
r = list(reversed(sorted(map(int, input().split()))))
print(main())
