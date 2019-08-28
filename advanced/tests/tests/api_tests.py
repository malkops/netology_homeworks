import unittest

import requests


def translate_text(text):
    token = 'trnsl.1.1.20190706T065851Z.f89e2545cf6aefc9.862181603af95861903c7ac23cd9cd9577db5166'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    response = requests.get(url, params={
        'key': token, 'lang': 'en-ru', 'text': text
    })

    return response.json()


class YandexTranslateTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.translate_dict = translate_text('hi')

    def test_url_available_success(self):
        res_code = self.translate_dict['code']
        self.assertTrue((200 <= res_code < 300))

    def test_url_available_failed(self):
        res_code = self.translate_dict['code']
        self.assertTrue((res_code < 200 or res_code >= 300))

    def test_translated_text(self):
        translated_text = set(self.translate_dict['text'])
        self.assertTrue(('привет' in translated_text))


if __name__ == '__main__':
    unittest.main()
