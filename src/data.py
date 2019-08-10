import csv
from os.path import isfile

PATH_DATA = '/home/marcosfilipe/dev/github/english-notebook/data/'
PATH_MEDIA_AUDIOS = '/home/marcosfilipe/dev/github/english-notebook/media/audios'
PATH_MEDIA_IMAGES = '/home/marcosfilipe/dev/github/english-notebook/media/images'


def load(source, path=PATH_DATA):
    path_full = path + source
    with open(path_full) as _file:
        csv_reader = csv.DictReader(_file, delimiter=';')
        data = list(csv_reader)
    return data


def audio(word, path=PATH_MEDIA_AUDIOS):
    file_name = '{}.mp3'.format(word)
    return (True, file_name) if isfile(path + '/' + file_name) else (False, '')


def image(word, path=PATH_MEDIA_IMAGES):
    file_names = ['{}.{}'.format(word, extension) for extension in ['jpeg', 'jpg', 'gif']]
    for file_name in file_names:
        if isfile(path + '/' + file_name):
            return True, file_name
    return False, ''
