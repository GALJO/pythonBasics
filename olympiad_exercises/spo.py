def count_occurrences(_text, _elements):
    _count = 0
    for letter in _text:
        if _elements.find(letter) != -1:
            _count += 1
    return _count


vowels = 'aąeęiouy'
text = input()

vowels_amount = count_occurrences(text, vowels)
consonants_amount = len(text) - vowels_amount

print('{} {}'.format(consonants_amount, vowels_amount))
