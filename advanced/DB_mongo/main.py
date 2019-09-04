import csv
import datetime
from pymongo import MongoClient


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        ticket_list = []
        for row in reader:
            row['Цена'] = int(row['Цена'])
            now_date = datetime.date.today()
            cur_year = now_date.year
            row['Дата'] = datetime.datetime.strptime(row['Дата'], "%d.%m")
            row['Дата'] = row['Дата'].replace(year=cur_year)
            ticket_list.append(dict(row))
        db.insert_many(ticket_list)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    cheapest_ticket = db.find({}, {'_id': 0}).sort('Цена', 1)
    for x in cheapest_ticket:
        print(x)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """
    result = db.find({'Исполнитель': {'$regex': name}}, {'_id': 0}).sort('Цена', 1)
    for x in result:
        print(x)


def find_by_date(db):
    start = datetime.datetime(2019, 7, 1)
    end = datetime.datetime(2019, 7, 30)
    result = db.find({'Дата': {'$gte': start, '$lte': end}}, {'_id': 0})
    for x in result:
        print(x)


if __name__ == '__main__':
    client = MongoClient()
    netology_db = client['guillotine']
    tickets_collection = netology_db['tickets']
    read_data('artists.csv', tickets_collection)

    print('Поиск билетов по возрастанию цены:')
    find_cheapest(tickets_collection)

    print('Поиск билетов по имени:')
    find_by_name('T-', tickets_collection)

    print('Поиск билетов по дате:')
    find_by_date(tickets_collection)
    tickets_collection.drop()
