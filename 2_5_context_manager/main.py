from contextlib import contextmanager
from datetime import datetime
import time


@contextmanager
def my_open(path, mod='r'):
    try:
        start = datetime.now()
        print('Начало работы: ', start)
        my_file = open(path, mod, encoding='utf-8')
        # time.sleep(10)
        yield my_file
        print('На выполнение потрачено: ', datetime.now() - start)
    finally:
        my_file.close()
        end = datetime.now()
        print('Конец работы: ', end)


with my_open('file.txt', 'a') as file:
    for i in [str(i)+str(i-1) for i in range(10)]:
        file.write(i + '\n')

print('\n\n')
with my_open('file.txt', 'r') as file:
    for line in file:
        print(line.replace('\n', ''))
