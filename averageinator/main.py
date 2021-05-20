import logging
import time
from math import floor, ceil

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s,%(msecs)d] [%(levelname)s]: %(message)s',
    datefmt='%H:%M:%S'
)


class Subject:
    def __init__(self, name, first_marks, first_weights, second_marks, second_weights):
        self.name = name
        self.first_marks = first_marks
        self.first_weights = first_weights
        self.second_marks = second_marks
        self.second_weights = second_weights
        self.first_average = None
        self.first_sum = None
        self.first_divider = None
        self.second_average = None
        self.second_sum = None
        self.second_divider = None
        self.average = None

    def count_first_average(self):
        logging.info('First average counting for {} subject started'.format(self.name))
        self.first_divider = 0
        self.first_sum = 0
        for _i in range(len(self.first_marks)):
            self.first_sum += self.first_marks[_i] * self.first_weights[_i]
            self.first_divider += self.first_weights[_i]
            logging.debug('[Iteration nr {}] Mark: {}'.format(_i + 1, self.second_marks[_i]))
            logging.debug('[Iteration nr {}] First sum: {}'.format(_i + 1, self.first_sum))
            logging.debug('[Iteration nr {}] First divider: {}'.format(_i + 1, self.first_divider))
            logging.debug('[Iteration nr {}] First average: {}'.format(_i + 1, self.first_sum / self.first_divider))
        self.first_average = self.first_sum / self.first_divider
        logging.info('First average count successfully ended with final result: {}'.format(self.first_average))

    def count_second_average(self):
        logging.info('Second average counting for {} subject started'.format(self.name))
        self.second_divider = 0
        self.second_sum = 0
        for _i in range(len(self.second_marks)):
            self.second_sum += self.second_marks[_i] * self.second_weights[_i]
            self.second_divider += self.second_weights[_i]
            logging.debug('[Iteration nr {}] Mark: {}'.format(_i + 1, self.second_marks[_i]))
            logging.debug('[Iteration nr {}] Second sum: {}'.format(_i + 1, self.second_sum))
            logging.debug('[Iteration nr {}] Second divider: {}'.format(_i + 1, self.second_divider))
            logging.debug('[Iteration nr {}] Second average: {}'.format(_i + 1, self.second_sum / self.second_divider))
        self.second_average = self.second_sum / self.second_divider
        logging.info('Second average count successfully ended with final result: {}'.format(self.second_average))

    def count_full_average(self):
        logging.info('Full average counting for {} subject started'.format(self.name))
        self.average = (self.first_sum + self.second_sum) / (self.first_divider + self.second_divider)
        logging.info('Full average count successfully ended with final result: {}'.format(self.average))


def input_reader():
    logging.info('Started reading input')
    _inp = open('input.in', 'r')
    logging.debug('Opened file {} in {} mode'.format('input.in', 'r'))
    _am_of_subjects = int(_inp.readline())
    logging.info('Read amount of subjects: {}'.format(_am_of_subjects))
    _subjects = []
    for _subject in range(_am_of_subjects):
        _subjects.append(Subject(
            name=_inp.readline(),
            first_marks=list(map(int, _inp.readline().split())),
            first_weights=list(map(int, _inp.readline().split())),
            second_marks=list(map(int, _inp.readline().split())),
            second_weights=list(map(int, _inp.readline().split()))
        ))
        logging.info('Read subject nr {}: {}'.format(_subject + 1, _subjects[_subject].name))
        logging.debug('First marks and weights: {} {}'.format(
            _subjects[_subject].first_marks,
            _subjects[_subject].first_weights
        ))
        logging.debug('Second marks and weights: {} {}'.format(
            _subjects[_subject].second_marks,
            _subjects[_subject].second_weights
        ))
    _inp.close()
    logging.debug('Closed file {}'.format('input.in'))
    return _am_of_subjects, _subjects


def first_main_average(_subjects, _am_of_subjects):
    logging.info('Started counting first main average')
    _result = 0
    for _subject in subjects:
        if _subject.first_average - floor(_subject.first_average) < 0.75:
            _result += floor(_subject.first_average)
            logging.debug('[Subject {}] Mark: {}'.format(_subject.name, floor(_subject.first_average)))
        else:
            _result += ceil(_subject.first_average)
            logging.debug('[Subject {}] Mark: {}'.format(_subject.name, ceil(_subject.first_average)))
        logging.debug('[Subject {}] Result: {}'.format(_subject.name, _result))
        logging.debug('[Subject {}] First main average: {}'.format(_subject.name, _result / _am_of_subjects))
    _result /= _am_of_subjects
    return _result


def second_main_average(_subjects, _am_of_subjects):
    logging.info('Started counting second main average')
    _result = 0
    for _subject in subjects:
        if _subject.second_average - floor(_subject.second_average) < 0.75:
            _result += floor(_subject.second_average)
            logging.debug('[Subject {}] Mark: {}'.format(_subject.name, floor(_subject.second_average)))
        else:
            _result += ceil(_subject.second_average)
            logging.debug('[Subject {}] Mark: {}'.format(_subject.name, ceil(_subject.second_average)))
        logging.debug('[Subject {}] Result: {}'.format(_subject.name, _result))
        logging.debug('[Subject {}] First main average: {}'.format(_subject.name, _result / _am_of_subjects))
    _result /= _am_of_subjects
    return _result


def full_main_average(_subjects, _am_of_subjects):
    logging.info('Started counting full main average')
    _result = 0
    for _subject in subjects:
        if _subject.average - floor(_subject.average) < 0.75:
            _result += floor(_subject.average)
            logging.debug('[Subject {}] Mark: {}'.format(_subject.name, floor(_subject.average)))
        else:
            _result += ceil(_subject.average)
            logging.debug('[Subject {}] Mark: {}'.format(_subject.name, ceil(_subject.average)))
        logging.debug('[Subject {}] Result: {}'.format(_subject.name, _result))
        logging.debug('[Subject {}] First main average: {}'.format(_subject.name, _result / _am_of_subjects))
    _result /= _am_of_subjects
    return _result


def output_saver(_subjects):
    logging.info('Started saving output')
    _out = open('output.out', 'a')
    logging.debug('Opened file {} in {} mode'.format('output.out', 'a'))
    _out.write('OUTPUT [{}]'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    _out.write('---------------------------')
    logging.debug('Written introduction')


logging.info(r'''
------------------------------------------------------------------------
    ___                                   _             __            
   /   |_   _____  _________ _____ ____  (_)___  ____ _/ /_____  _____
  / /| | | / / _ \/ ___/ __ `/ __ `/ _ \/ / __ \/ __ `/ __/ __ \/ ___/
 / ___ | |/ /  __/ /  / /_/ / /_/ /  __/ / / / / /_/ / /_/ /_/ / /    
/_/  |_|___/\___/_/   \__,_/\__, /\___/_/_/ /_/\__,_/\__/\____/_/     
                           /____/                                     
------------------------------------------------------------------------
''')

logging.info('Session started: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
amount_of_subjects, subjects = input_reader()
logging.info('Input read successfully')

for subject in subjects:
    subject.count_first_average()
    subject.count_second_average()
    subject.count_full_average()

main_averages = {}
main_averages.setdefault('average1', first_main_average(subjects, amount_of_subjects))
logging.info('First main average counted successfully with result: {}'.format(main_averages['average1']))
main_averages.setdefault('average2', second_main_average(subjects, amount_of_subjects))
logging.info('Second main average counted successfully with result: {}'.format(main_averages['average2']))
main_averages.setdefault('average_main', full_main_average(subjects, amount_of_subjects))
logging.info('Full main average counted successfully with result: {}'.format(main_averages['average_main']))
