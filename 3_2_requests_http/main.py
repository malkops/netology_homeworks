import requests

API_KEY = 'trnsl.1.1.20190706T065851Z.f89e2545cf6aefc9.862181603af95861903c7ac23cd9cd9577db5166'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def save_translate_in_file(file: str, translate: str) -> None:
    """
    Сохранить перевод в файл
    :param file:
    :param translate:
    :return: None
    """
    with open(file, 'w') as file_write:
        file_write.write(translate)


def read_text_from_file(file: str) -> str:
    """
    Получить текст из файла
    :param file:
    :return: str
    """
    text = ''
    with open(file, 'r') as file_read:
        for line in file_read.read():
            text += line

    return text


def translate_it(load_file: str, dump_file: str, to_lang='ru', from_lang='') -> None:
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param load_file:
    :param dump_file:
    :param to_lang:
    :param from_lang:
    :return: None
    """
    lang = f'{from_lang}-{to_lang}' if from_lang != '' else to_lang
    text = read_text_from_file(load_file)

    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang,
    }

    try:
        response = requests.get(URL, params=params)
    except ConnectionError as ce:
        print('Connection Error (exception):', ce)
        return

    json_ = response.json()
    translate = ''.join(json_['text'])

    save_translate_in_file(dump_file, translate)

    return


# список переводимых файлов
file_names = ['DE.txt', 'ES.txt', 'FR.txt']
# переводим каждый файл
for file in file_names:
    translate_it(file, f'{file}_translated')
