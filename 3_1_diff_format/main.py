import json
import xml.etree.ElementTree as ET


def check_in_strict(strict, word) -> None:
    """
    Проверяет, есть ли переданное слово в словаре всех слов.
    Увеличивает счетчик или добавляет слово в словарь.
    :param strict: словарь, содержащий все слова
    :param word: слово
    :return: None
    """
    if word in strict.keys():
        strict.update([(word, strict[word] + 1)])
    else:
        strict[word] = 1
    return


def json_top_words() -> str:
    """
    Работает с json форматом.
    Возвращает строку, которая содержит
    10 самых часто используемых слов в статьях через пробел
    :return: str
    """
    json_words = {}
    with open("newsafr.json", "r") as read_file:
        data = json.load(read_file)
    for item in data['rss']['channel']['items']:
        for word in item['description'].lower().split():
            check_in_strict(json_words, word)
    json_words = sorted(json_words.items(), key=lambda kv: kv[1], reverse=True)
    return ' '.join([x[0] for x in json_words[:11]])


def xml_top_words() -> str:
    """
    Работает с xml форматом.
    Возвращает строку, которая содержит
    10 самых часто используемых слов в статьях через пробел.
    :return: str
    """
    xml_words = {}
    tree = ET.ElementTree(file='newsafr.xml')
    for item in tree.findall('channel/item'):
        for word in item.find('description').text.lower().split():
            check_in_strict(xml_words, word)
    xml_words = sorted(xml_words.items(), key=lambda kv: kv[1], reverse=True)
    return ' '.join([x[0] for x in xml_words[:11]])


if __name__ == '__main__':
    print("Слова из json'а:", json_top_words())
    print("Слова из xml'я:", xml_top_words())
