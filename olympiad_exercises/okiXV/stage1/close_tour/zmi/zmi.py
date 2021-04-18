# https://szkopul.edu.pl/problemset/problem/uMEWCEG1XvCB2bZckVDJyk1i/site/?key=statement


def is_word_floating_letter(_word):
    for _i in range(len(_word)):
        if _i == 0:
            continue
        if _word[_i - 1] == _word[_i]:
            return False
    return True


word = input()
correct_words = set()
amount_of_ways = 0
amount_of_ways_in_iter = 0
for i in range(len(word)):
    if i != 0 and word[i - 1] == word[i]:
        amount_of_ways += amount_of_ways_in_iter
        continue
    if i != 0 and amount_of_ways_in_iter == 0:
        break
    amount_of_ways_in_iter = 0
    for j in range(i + 1, len(word)):
        for n in range(j + 1, len(word)):
            _actual_word = word[i] + word[j] + word[n]
            if is_word_floating_letter(_actual_word):
                correct_words.add(_actual_word)
                amount_of_ways += 1
                amount_of_ways_in_iter += 1

print('{} {}'.format(amount_of_ways, len(correct_words)))
