import logging
import time
from math import floor, ceil

logging.basicConfig(
    level=logging.INFO,
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
        self.first_sem_average = None
        self.first_sum = None
        self.first_divider = None
        self.second_sem_average = None
        self.second_sum = None
        self.second_divider = None
        self.year_average = None

    def count_first_semester_average(self):
        logging.info('[{}] First semester average counting started'.format(self.name))
        self.first_divider = 0
        self.first_sum = 0
        for _i in range(len(self.first_marks)):
            self.first_sum += self.first_marks[_i] * self.first_weights[_i]
            self.first_divider += self.first_weights[_i]
            logging.debug('[Iteration nr {}] Mark: {}'.format(_i + 1, self.first_marks[_i]))
            logging.debug('[Iteration nr {}] First sum: {}'.format(_i + 1, self.first_sum))
            logging.debug('[Iteration nr {}] First divider: {}'.format(_i + 1, self.first_divider))
            logging.debug('[Iteration nr {}] First average: {}'.format(_i + 1, self.first_sum / self.first_divider))
        self.first_sem_average = self.first_sum / self.first_divider
        logging.info('[{}] First semester average counted successfully with final result: {}'.format(self.name,
                                                                                                     self.first_sem_average))

    def count_second_semester_average(self):
        logging.info('[{}] Second semester average counting started'.format(self.name))
        self.second_divider = 0
        self.second_sum = 0
        for _i in range(len(self.second_marks)):
            self.second_sum += self.second_marks[_i] * self.second_weights[_i]
            self.second_divider += self.second_weights[_i]
            logging.debug('[Iteration nr {}] Mark: {}'.format(_i + 1, self.second_marks[_i]))
            logging.debug('[Iteration nr {}] Second sum: {}'.format(_i + 1, self.second_sum))
            logging.debug('[Iteration nr {}] Second divider: {}'.format(_i + 1, self.second_divider))
            logging.debug('[Iteration nr {}] Second average: {}'.format(_i + 1, self.second_sum / self.second_divider))
        self.second_sem_average = self.second_sum / self.second_divider
        logging.info('[{}] First semester average counted successfully with final result: {}'.format(self.name,
                                                                                                     self.first_sem_average))

    def count_year_average(self):
        logging.info('[{}] Year average counting started'.format(self.name))
        self.year_average = (self.first_sum + self.second_sum) / (self.first_divider + self.second_divider)
        logging.info('[{}] Year average counted successfully with final result: {}'.format(self.name,
                                                                                           self.first_sem_average))


def input_reader():
    logging.info('Started reading input')
    _inp = open('input.in', 'r')
    logging.debug('Opened file {} in {} mode'.format('input.in', 'r'))
    _am_of_subjects = int(_inp.readline())
    logging.info('Read amount of subjects: {}'.format(_am_of_subjects))
    _subjects = []
    for _subject in range(_am_of_subjects):
        _subjects.append(Subject(
            name=_inp.readline()[:-1],
            first_marks=list(map(float, _inp.readline().split())),
            first_weights=list(map(int, _inp.readline().split())),
            second_marks=list(map(float, _inp.readline().split())),
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


def count_first_semester_final(_subjects, _am_of_subjects):
    logging.info('Started counting first main average')
    _result = 0
    for _subject in subjects:
        if _subject.first_sem_average - floor(_subject.first_sem_average) < 0.75:
            _result += floor(_subject.first_sem_average)
            logging.debug('[Subject {}] Mark: {} ({})'.format(_subject.name, floor(_subject.first_sem_average),
                                                              _subject.first_sem_average))
        else:
            _result += ceil(_subject.first_sem_average)
            logging.debug('[Subject {}] Mark: {} ({})'.format(_subject.name, ceil(_subject.first_sem_average),
                                                              _subject.first_sem_average))
        logging.debug('[Subject {}] Result: {}'.format(_subject.name, _result))
        logging.debug('[Subject {}] First main average: {}'.format(_subject.name, _result / _am_of_subjects))
    _result /= _am_of_subjects
    return _result


def count_second_semester_final(_subjects, _am_of_subjects):
    logging.info('Started counting second main average')
    _result = 0
    for _subject in subjects:
        if _subject.second_sem_average - floor(_subject.second_sem_average) < 0.75:
            _result += floor(_subject.second_sem_average)
            logging.debug('[Subject {}] Mark: {} ({})'.format(_subject.name, floor(_subject.second_sem_average),
                                                              _subject.second_sem_average))
        else:
            _result += ceil(_subject.second_sem_average)
            logging.debug('[{}] Mark: {} ({})'.format(_subject.name, ceil(_subject.second_sem_average),
                                                      _subject.second_sem_average))
        logging.debug('[{}] Result: {}'.format(_subject.name, _result))
        logging.debug('[Subject {}] First main average: {}'.format(_subject.name, _result / _am_of_subjects))
    _result /= _am_of_subjects
    return _result


def count_year_final(_subjects, _am_of_subjects):
    logging.info('Started counting full main average')
    _result = 0
    for _subject in subjects:
        if _subject.year_average - floor(_subject.year_average) < 0.75:
            _result += floor(_subject.year_average)
            logging.debug('[Subject {}] Mark: {} ({})'.format(_subject.name, floor(_subject.year_average),
                                                              _subject.year_average))
        else:
            _result += ceil(_subject.year_average)
            logging.debug(
                '[Subject {}] Mark: {} ({})'.format(_subject.name, ceil(_subject.year_average), _subject.year_average))
        logging.debug('[Subject {}] Result: {}'.format(_subject.name, _result))
        logging.debug('[Subject {}] First main average: {}'.format(_subject.name, _result / _am_of_subjects))
    _result /= _am_of_subjects
    return _result


def output_saver(_subjects, _main_averages):
    logging.info('Started saving output')
    _out = open('output.out', 'a')
    logging.debug('Opened file {} in {} mode'.format('output.out', 'a'))
    _out.write('OUTPUT [{}]\n'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
    _out.write('---------------------------\n')
    logging.info('Written introduction')
    _out.write('First semester averages:\n')
    for _subject in subjects:
        _out.write('[{}]: {}\n'.format(_subject.name, round(_subject.first_sem_average, 2)))
        logging.debug('[{}] Written first average'.format(_subject.name))
    _out.write('---------------------------\n')
    logging.info('Written first semester averages')

    _out.write('Second semester averages:\n')
    for _subject in subjects:
        _out.write('[{}]: {}\n'.format(_subject.name, round(_subject.second_sem_average, 2)))
        logging.debug('[{}] Written second average'.format(_subject.name))
    _out.write('---------------------------\n')
    logging.info('Written second semester averages')

    _out.write('Year averages:\n')
    for _subject in subjects:
        _out.write('[{}]: {}\n'.format(_subject.name, round(_subject.year_average, 2)))
        logging.debug('[{}] Written second average'.format(_subject.name))
    _out.write('---------------------------\n')
    logging.info('Written year averages')

    _out.write('Final semesters averages:\n')
    _out.write('[First semester]: {}\n'.format(round(_main_averages['first_semester_final'], 2)))
    _out.write('[Second semester]: {}\n'.format(round(_main_averages['second_semester_final'], 2)))
    _out.write('---------------------------\n')
    logging.info('Written final semesters averages')

    _out.write('FINAL YEAR AVERAGE: {}\n'.format(round(_main_averages['year_final'], 2)))
    if _main_averages['year_final'] > 4.75:
        _out.write('RED STRIPE :DD\n')
        logging.debug('Main average > 4.75 so we have red stripe')
    else:
        _out.write('NO RED STRIPE YET DD:\n')
        logging.debug("Main average < 4.75 so we haven't red stripe")
    _out.write('---------------------------\n\n')
    logging.info('Written final year average')
    _out.close()
    logging.debug('Closed file {}'.format('output.out'))
    logging.info('Saved output successfully')


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
    subject.count_first_semester_average()
    subject.count_second_semester_average()
    subject.count_year_average()

final_averages = {}
final_averages.setdefault('first_semester_final', count_first_semester_final(subjects, amount_of_subjects))
logging.info('First semester final counted successfully with result: {}'.format(final_averages['first_semester_final']))
final_averages.setdefault('second_semester_final', count_second_semester_final(subjects, amount_of_subjects))
logging.info(
    'Second semester final counted successfully with result: {}'.format(final_averages['second_semester_final']))
final_averages.setdefault('year_final', count_year_final(subjects, amount_of_subjects))
logging.info('Year final counted successfully with result: {}'.format(final_averages['year_final']))

output_saver(subjects, final_averages)
logging.info('Session ended: {}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))