def validate_quality(_text):
    if _text == 'l':
        return 360
    elif _text == 'm':
        return 480
    elif _text == 'h':
        return 720
    else:
        return 'err'