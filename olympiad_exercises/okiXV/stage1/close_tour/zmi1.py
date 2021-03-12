# https://szkopul.edu.pl/problemset/problem/uMEWCEG1XvCB2bZckVDJyk1i/site/?key=submissions - 0% points

def main():
    dict_ = {}
    if len(set(word)) < 2:
        return 0, 0
    for i in range(len(word) - 2):
        for j in range(i + 1, len(word) - 1):
            for n in range(j + 1, len(word)):
                if word[i] != word[j] and word[j] != word[n]:
                    key = word[i] + word[j] + word[n]
                    dict_.setdefault(key, 0)
                    dict_[key] += 1
    sum_ = 0
    keys = list(dict_.keys())
    for key in keys:
        sum_ += dict_[key]
    return sum_, dict_


word = list(map(str, input()))
tuple_ = main()
print(tuple_[0], tuple_[1])