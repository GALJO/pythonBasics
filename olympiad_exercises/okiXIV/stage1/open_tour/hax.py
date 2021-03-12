# https://szkopul.edu.pl/problemset/problem/-sW59iNCsLGhh8xyFPEmtn7F/site/?key=statement - 100% points

def main():
    _hax_text = ''
    for _i in range(len(normal_text)):
        if normal_text[_i] == 'a':
            _hax_text += '4'
        elif normal_text[_i] == 'e':
            _hax_text += '3'
        elif normal_text[_i] == 'i':
            _hax_text += '1'
        elif normal_text[_i] == 'o':
            _hax_text += '0'
        elif normal_text[_i] == 's':
            _hax_text += '5'
        else:
            _hax_text += normal_text[_i]
    return _hax_text


normal_text = input()
print(main())
