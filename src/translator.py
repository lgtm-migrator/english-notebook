from googletrans import Translator


class Translator(object):
    _translator = translator = Translator(service_urls=[
        'translate.google.com',
    ])

    _dest = 'pt'

    def text(self, text):
        o = self._translator.translate(text, dest=self._dest)
        return o.text
