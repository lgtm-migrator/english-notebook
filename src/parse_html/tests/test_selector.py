from unittest import TestCase
from parsel import Selector


class SelectorCase(TestCase):

    def test_selector_search_base(self):
        text = u"""
        <html>
            <body>
                <h1>Hello, Parsel!</h1>
            </body>
        </html>
        """
        selector = Selector(text=text)

        self.assertEqual(selector.xpath('//h1').get(), '<h1>Hello, Parsel!</h1>')
        self.assertEqual(selector.css('h1').get(), '<h1>Hello, Parsel!</h1>')

    def test_selector_function_call(self):
        text = u"""
        <html>
            <body>
                <h1>Hello, Parsel!</h1>
            </body>
        </html>
        """

        selector = Selector(text=text)

        self.assertEqual(selector.xpath('//h1/text()').get(), 'Hello, Parsel!')
        self.assertEqual(selector.css('h1::text').get(), 'Hello, Parsel!')

    def test_selector_html_complete(self):

        html = """
        <html>
            <head>
                <base href='http://example.com/' />
                <title>Example website</title>
            </head>
            <body>
                <div id='images'>
                    <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
                    <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
                    <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
                    <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
                    <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
                </div>
            </body>
        </html>
        """
        selector = Selector(text=html)

        # assert title
        self.assertEqual(selector.xpath('//title/text()').get(), 'Example website')
        self.assertEqual(selector.css('title::text').get(), 'Example website')

        print(selector.xpath('//img/@src').getall())
        
    def test_english_words(self):
        
        import requests
        
        text = requests.get('https://www.englishspeak.com/en/english-words').text
        selector = Selector(text=text)
        sounds = selector.xpath('//img/@onclick').getall()
            

