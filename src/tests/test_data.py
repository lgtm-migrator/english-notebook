from unittest import TestCase
from data import load, image, audio

from os import path


class DataTest(TestCase):

    def test_load(self):
        verbs = load('verbs')
        self.assertTrue(len(verbs) > 0)

    def test_x(self):
        self.assertTrue(path.isfile('/home/marcosfilipe/dev/github/english-notebook/media/images/go.jpg'))

    def test_is_images_exist(self):
        self.assertEqual(image('go'), (True, 'go.jpg'))
        self.assertEqual(image('xxx'), (False, ''))

    def test_is_audio_exist(self):
        self.assertEqual(audio('go'), (True, 'go.mp3'))
        self.assertEqual(audio('xxx'), (False, ''))
