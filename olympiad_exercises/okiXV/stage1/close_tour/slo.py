# https://szkopul.edu.pl/problemset/problem/X_c5-zBjq7K3WVRw17khA520/site/?key=statement - 69% points

def convert_to_numbers(_words, _dict):
    """
    Zamienia tablice liczb napisanych slownie na tablice liczb korzystajac ze slownika pomocniczego dict_. Zwraca 'NIE' 
    jeżeli slowo zostanie nierozpoznane.
    :param _words: lista slow
    :param _dict: slownik pomocniczy z liczbami slownymi i ich numerycznymi wartosciami
    :return: tablica liczb lub 'NIE'
    """
    _dict_keys = list(_dict.keys())
    _res = []
    for _i in range(len(_words)):
        for _j in range(len(_dict_keys)):
            if _words[_i] == _dict_keys[_j]:
                _res.append(_dict.get(_dict_keys[_j]))
                break
            if _j == len(_dict_keys) - 1:
                return 'NIE'
    return _res


def convert_to_groups(_numbers):
    """
    Zamienia liste liczb na grupy miliardow, milionow, tysiecy, setek
    :param _numbers: lista liczb
    :return: tablica grup
    """
    _res = []
    _mld = 0
    _mln = 0
    _k = 0
    _hund = 0
    if len(_numbers) == 1:
        _hund = _numbers[0]
        _res = [_mld, _mln, _k, _hund]
        return _res
    _i = 0
    for _i in range(len(_numbers)):
        if _numbers[_i] == 1000000000:
            for _md in range(_i - 1, -1, -1):
                _mld += _numbers[_md]
            _mld = _mld * 1000000000
            continue
        if _numbers[_i] == 1000000:
            for _m in range(_i - 1, -1, -1):
                if _numbers[_m] == 1000000000:
                    break
                _mln += _numbers[_m]
            _mln = _mln * 1000000
            continue
        elif _numbers[_i] == 1000:
            for _ki in range(_i - 1, -1, -1):
                if _numbers[_ki] == 1000000:
                    break
                if _numbers[_ki] == 1000000000:
                    break
                _k += _numbers[_ki]
            _k = _k * 1000
            continue
    for _j in range(len(_numbers) - 1, -1, -1):
        if _numbers[_j] == 1000 or _numbers[_j] == 1000000 or _numbers[_j] == 1000000000:
            break
        _hund += _numbers[_j]
    _res = [_mld, _mln, _k, _hund]
    return _res


def validate_syntax(_numbers, _words):
    """
    Sprawdza poprawnosc skladni.
    :param _numbers: lista liczb
    :param _words: lista slow
    :return: True jeżeli nie ma bledow, w przeciwnym wypadku False.
    """
    _were_million = False
    _were_thousand = False
    _were_hundreds = False
    _were_tens = False
    _were_ones = False
    for _i in range(len(_numbers)):
        # billiards, millions and thousands
        if _numbers[_i] == 1000000000:
            if len(_numbers) != 2:
                return False
            if _numbers[_i - 1] != 1:
                return False
            if _were_million:
                return False
            if _were_thousand:
                return False
        if _numbers[_i] == 1000000:
            if len(_numbers) == 1:
                return False
            if _i - 1 == -1:
                return False
            if _were_million:
                return False
            if _were_thousand:
                return False
            if _words[_i] == 'milion' and _numbers[_i - 1] != 1:
                return False
            if _words[_i] == 'miliony' and (_numbers[_i - 1] > 4 or 2 > _numbers[_i - 1]):
                return False
            if _words[_i] == 'milionow' and _numbers[_i - 1] < 5:
                return False
            _were_million = True
        if _numbers[_i] == 1000:
            if len(_numbers) == 1:
                return False
            if _i - 1 == -1:
                return False
            if _were_thousand:
                return False
            _were_thousand = True
            if _words[_i] == 'tysiac' and _numbers[_i - 1] != 1:
                return False
            if _words[_i] == 'tysiace' and (_numbers[_i - 1] > 4 or 2 > _numbers[_i - 1]):
                return False
            if _words[_i] == 'tysiecy' and _numbers[_i - 1] < 5:
                return False
    # hundreds, tens and ones
    for _i in range(len(_numbers) - 1, -1, -1):
        if _numbers[_i] == 1000 or _numbers[_i] == 1000000 or _numbers[_i] == 1000000000:
            break
        if len(str(_numbers[_i])) == 3:
            if _were_hundreds:
                return False
            _were_hundreds = True
        if len(str(_numbers[_i])) == 2:
            if _were_tens:
                return False
            if _were_hundreds:
                return False
            _were_tens = True
        if len(str(_numbers[_i])) == 1:
            if _were_ones:
                return False
            if _were_tens:
                return False
            if _were_hundreds:
                return False
            _were_ones = True
    return True


def main():
    """
    Glowna metoda obliczeniowa programu.
    """
    _converted_numb = 0
    _numb_list = convert_to_numbers(numb_in_words_list, dict_)
    if _numb_list == 'NIE':
        return _numb_list
    if not validate_syntax(_numb_list, numb_in_words_list):
        return 'NIE'
    _numb_groups = convert_to_groups(_numb_list)
    for _group in _numb_groups:
        _converted_numb += _group
    return _converted_numb


numb_in_words_list = input().split()
dict_ = {
    'jeden': 1,
    'dwa': 2,
    'trzy': 3,
    'cztery': 4,
    'piec': 5,
    'szesc': 6,
    'siedem': 7,
    'osiem': 8,
    'dziewiec': 9,
    'dziesiec': 10,
    'jedenascie': 11,
    'dwanascie': 12,
    'trzynascie': 13,
    'czternascie': 14,
    'pietnascie': 15,
    'szesnascie': 16,
    'siedemnascie': 17,
    'osiemnascie': 18,
    'dziewietnascie': 19,
    'dwadziescia': 20,
    'trzydziesci': 30,
    'czterdziesci': 40,
    'piecdziesiat': 50,
    'szescdziesiat': 60,
    'siedemdziesiat': 70,
    'osiemdziesiat': 80,
    'dziewiecdziesiat': 90,
    'sto': 100,
    'dwiescie': 200,
    'trzysta': 300,
    'czterysta': 200,
    'piecset': 500,
    'szescset': 600,
    'siedemset': 700,
    'osiemset': 800,
    'dziewiecset': 900,
    'tysiac': 1000,
    'tysiace': 1000,
    'tysiecy': 1000,
    'milion': 1000000,
    'miliony': 1000000,
    'milionow': 1000000,
    'miliard': 1000000000,
    'miliardy': 1000000000,
    'miliardow': 1000000000
}


print(main())
