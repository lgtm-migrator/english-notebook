import requests
from parsel import Selector
import wget


def dowload_english_speak(url, pages):
    for i in range(1, 21):
        text = requests.get(url.format(i)).text
        selector = Selector(text)
        for brute_sound in selector.xpath('//img/@onclick').getall():
            brute_sound = brute_sound[22:-2]
            if 'english/phrases/slow/' not in brute_sound:
                file_name = brute_sound.split('/')[-1]
                try:
                    print('ok: ' + brute_sound)
                    wget.download(url=brute_sound,
                              out='/home/mfilipelino/dev/github/english-notebook/data/audios/worlds/' + file_name)
                except:
                    print('erro:' + brute_sound)


def conversation():
    for i in range(200):
        try:
            wget.download(
                url="https://dcgm6jfwtvdqr.cloudfront.net/instantspeak/english/lessons/conversations/mp3/{}.mp3".format(i),
                out='/home/mfilipelino/dev/github/english-notebook/data/audios/conversations/{}.mp3'.format(i)
            )
        except:
            pass


if __name__ == '__main__':
    # dowload_english_speak(
    #     url='https://www.englishspeak.com/en/english-phrases?category_key={}',
    #     pages=range(22)
    # )
    # dowload_english_speak(
    #     url='https://www.englishspeak.com/en/english-words?category_key={}',
    #     pages=range(22)
    # )
    conversation()