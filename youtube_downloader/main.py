import pytube
import logging
import time


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
            logging.warning('Changed resolution by -1 ({})'.format(resolutions[_res_ndx]))
        else:
            return _actual_stream, _res_ndx


def write_ascii_art():
    print('------------------------------')
    time.sleep(0.2)
    print()
    time.sleep(0.2)
    print('\ \ / /         | |       | |          |  _  \                  | |               | |          ')
    time.sleep(0.2)
    print(' \ V /___  _   _| |_ _   _| |__   ___  | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ ')
    time.sleep(0.2)
    print("  \ // _ \| | | | __| | | | '_ \ / _ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    time.sleep(0.2)
    print('  | | (_) | |_| | |_| |_| | |_) |  __/ | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ')
    time.sleep(0.2)
    print('  \_/\___/ \__,_|\__|\__,_|_.__/ \___| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ')
    time.sleep(0.2)
    print()
    time.sleep(0.2)
    print('------------------------------')
    logging.info('------------------------------')
    logging.info(' ')
    logging.info('\ \ / /         | |       | |          |  _  \                  | |               | |          ')
    logging.info(' \ V /___  _   _| |_ _   _| |__   ___  | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ ')
    logging.info("  \ // _ \| | | | __| | | | '_ \ / _ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    logging.info('  | | (_) | |_| | |_| |_| | |_) |  __/ | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ')
    logging.info('  \_/\___/ \__,_|\__|\__,_|_.__/ \___| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ')
    logging.info(' ')
    logging.info('------------------------------')


def download_actual_stream(_stream, _res):
    print('Rozpoczęto pobieranie')
    _stream.download('downloads')
    print('Pobrano pomyślnie w jakości {}p'.format(resolutions[actual_res_ndx]))


logging.basicConfig(format='(%(asctime)s) - %(levelname)s: %(message)s', datefmt='%d-%m %H:%M:%S', filename='log.log')
resolutions = ['144', '240', '360', '480', '720']
write_ascii_art()
amount_of_links = int(input('Podaj liczbę filmów którą chcesz pobrać >> '))
logging.info('USERINPUT: Q: Podaj liczbę filmów którą chcesz pobrać >> A: {}'.format(amount_of_links))
print('Podaj listę linków i jakości (max. 720p) oddzielonych enterem')
logging.info('USERINPUT: Q: Podaj listę linków i jakości (max. 720p) oddzielonych enterem >> A: ')

list_ = []
for i in range(amount_of_links * 2):
    list_.append(input())

logging.info('{}'.format(list_))

print("----")
print()

counter = 0
done = 0
for i in range(0, amount_of_links * 2, 2):
    counter += 1
    logging.info('Started action for video {}/{}'.format(counter, amount_of_links))
    print('Pobieranie filmu {}/{}'.format(counter, amount_of_links))
    actual_url = pytube.YouTube(list_[i])
    logging.info('URL downloaded')
    actual_res_ndx = validate_correct_of_res(list_[i + 1][:-1])
    logging.info('Successfully validated resolution')
    actual_streams = actual_url.streams.filter(progressive=True, file_extension='mp4')

    actual_stream, actual_res_ndx = find_the_best_stream(actual_res_ndx)
    if actual_res_ndx == -1:
        print('Wystąpił błąd: brak odpowiedniej jakości')
        print('----')
        print()
        logging.error(
            'Resolution for video {}/{} not founded, continuing to next video'.format(counter, amount_of_links))
        continue

    logging.info('Started Downloading')
    download_actual_stream(actual_stream[0], resolutions[actual_res_ndx])
    done += 1
    logging.info('Successfully downloaded in {}p'.format(resolutions[actual_res_ndx]))
    print('----')
    print()

print('ZAKOŃCZONO DZIAŁANIE PROGRAMU')
print('Pobrania zakończone sukcesem: {}'.format(done))
print('Pobrania zakończone błędem: {}'.format(amount_of_links - done))
logging.info('Successfully downlaoded - {}'.format(done))
logging.info('Not downloaded (Error) - {}'.format(amount_of_links - done))
logging.info('Successfully exited with code 0')
