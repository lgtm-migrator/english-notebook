#!/usr/bin/python3

import wget
import sys


def tatoeba(id):
    out = 'media/{name}.mp3'
    url_base = 'https://audios.tatoeba.org/sentences/eng/{}.mp3'
    wget.download(url=url_base.format(id), out=out.format(name=id + '-aa'))


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 2:
        id = sys.argv[1]
        tatoeba(id)
        print()
