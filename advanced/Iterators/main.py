import json
import wikipedia
import hashlib
from tqdm import tqdm


class MyIterator:
    def __init__(self, input_file):
        with open(input_file, 'r', encoding='utf-8') as f:
            self.input_json = json.loads(f.read())
        self.end_file = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_file + 1 >= len(self.input_json):
            raise StopIteration
        self.end_file += 1
        return self.input_json[self.end_file].get('name').get('common')


def my_md5_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as rfile:
        for line in rfile:
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    # using iterator (example)
    with open('result.txt', 'w', encoding='utf-8') as fwrite:
        for item in tqdm(MyIterator('countries.json')):
            try:
                fwrite.write(f"{item} - {wikipedia.page(item).url}\n")
            except wikipedia.exceptions.DisambiguationError:
                fwrite.write(f"{item} - {wikipedia.page(item + ' (country)').url}\n")
    print('------------generator-----------')
    # using generator (example)
    for string in my_md5_generator('test_md5.txt'):
        print(string)
