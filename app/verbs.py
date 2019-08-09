from translator import Translator
from data import load, audio, image


def view_csv(word, ptbr, audio, image, pos):
    return '{};{};{};{};{}'.format(word, ptbr, audio, image, pos)


def view_cli(word, ptbr, audio, image, pos):
    return '{:15};{:15};{:15};{:15};{:15}'.format(word, ptbr, audio, image, pos)


def csv_generator():
    translator = Translator()
    print('{};{};{};{};{}'.format('word', 'ptbr', 'audio', 'image', 'pos'))
    for data in load('verbs'):
        verb = data['verb']
        _, _audio = audio(verb)
        _, _image = image(verb)
        ptbr = translator.text('to ' + verb)
        print(view_csv(verb, ptbr, _audio, _image, 'verb'))


def main():
    for data in load('verbs.csv'):
         print(view_csv(**data))


if __name__ == '__main__':
    main()
