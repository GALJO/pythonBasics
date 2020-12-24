import pytube


def validate_correct_of_res(_res):
    try:
        _res = resolutions.index(_res)
    except ValueError:
        return 'ValueErr'
    return _res


def find_the_best_stream(_res_ndx):
    while _res_ndx != -1:
        _actual_stream = actual_streams.filter(res='{}p'.format(resolutions[_res_ndx]))
        if len(_actual_stream) == 0:
            _res_ndx -= 1
        else:
            return _actual_stream, _res_ndx


def download_actual_stream(_stream, _res):
    print('Rozpoczęto pobieranie')
    _stream.download('downloads')
    print('Pobrano pomyślnie w jakości {}p'.format(resolutions[actual_res_ndx]))


resolutions = ['144', '240', '360', '480', '720']
print('Youtube Downloader')
print('----')
print()
amount_of_links = int(input('Podaj liczbę filmów którą chcesz pobrać >> '))
print('Podaj listę linków i jakości (max. 720p) oddzielonych enterem')

list_ = []

for i in range(amount_of_links * 2):
    list_.append(input())

print("----")
print()

counter = 0
done = 0
for i in range(0, amount_of_links * 2, 2):
    counter += 1
    print('Pobieranie filmu {}/{}'.format(counter, amount_of_links))
    actual_url = pytube.YouTube(list_[i])
    actual_res_ndx = validate_correct_of_res(list_[i + 1][:-1])
    actual_streams = actual_url.streams.filter(progressive=True, file_extension='mp4')

    actual_stream, actual_res_ndx = find_the_best_stream(actual_res_ndx)
    if actual_res_ndx == -1:
        print('Wystąpił błąd: brak odpowiedniej jakości')
        print('----')
        print()
        continue

    download_actual_stream(actual_stream[0], resolutions[actual_res_ndx])
    done += 1
    print('----')
    print()

print('ZAKOŃCZONO DZIAŁANIE PROGRAMU')
print('Pobrania zakończone sukcesem: {}'.format(done))
print('Pobrania zakończonych błędem: {}'.format(amount_of_links - done))
