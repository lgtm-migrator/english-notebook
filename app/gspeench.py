from google_speech import Speech
import sys


def speech(text, lang='en'):
    s = Speech(text, lang)
    s.play()
    s.save('media/{}.mp3'.format(text))


#"//body//div//span[@class='icon icon-audios']"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        text = sys.argv[1]
        speech(text)
