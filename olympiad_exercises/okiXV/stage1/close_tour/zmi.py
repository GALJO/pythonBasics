def sum_letters():
    """
    Oblicza ilosc wystapien kazdego znaku ze slowa.
    :return: slownik z iloscia wystapien
    """
    _res = {}
    for _i in range(len(word)):
        _res.setdefault(word[_i], 0)
        _res[word[_i]] += 1
    return _res


def sum_other_parts(_sums):
    for _i in range(1, len(word)):
        _sums.append({})
        _sums[_i].update(_sums[_i - 1])
        _sums[_i][word[_i - 1]] -= 1
    return _sums


def count_three_letters_words():
    _res = {}
    for _i in range(1, len(word)):
        _actual = [word[_i - 1], word[_i]]
        if _actual[0] == _actual[1]:
            continue
        for _j in range(len(sums[_i])):
            _keys = list(sums[_i].keys())
            if _keys[_j] == _actual[1]:
                continue
            if sums[_i][_keys[_j]] == 0:
                continue
            _res.setdefault(word[_i - 1] + word[_i] + _keys[_j], 0)
            _res[word[_i - 1] + word[_i] + _keys[_j]] += sums[_i][_keys[_j]]
    return _res


word = list(map(str, input()))
sums = [sum_letters()]
sums = sum_other_parts(sums)
three_letters_words_dict = count_three_letters_words()

amount_of_letter_positions = 0
amount_of_words = 0

three_letters_words_dict_keys = list(three_letters_words_dict.keys())
for i in range(len(three_letters_words_dict_keys)):
    amount_of_words += 1
    amount_of_letter_positions += three_letters_words_dict[three_letters_words_dict_keys[i]]

print(amount_of_letter_positions, end=' ')
print(amount_of_words, end='')

#print(three_letters_words_dict)
