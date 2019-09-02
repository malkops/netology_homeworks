import csv
import os
import re


def read_csv_data(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as opened_file:
        rows = csv.reader(opened_file, delimiter=',')
        return list(rows)


def save_new_csv_data(path_to_file, data_list):
    rows = [['lastname', 'firstname', 'surename', ' organization', 'position', 'phone', 'email']]
    for dict_item in data_list:
        sub_list = list(dict_item.values())
        row = sub_list[:1][0]
        row.extend(sub_list[1:len(sub_list)])
        rows.append(row)
    with open(path_to_file, 'w', newline='', encoding='utf-8') as opened_file:
        writer = csv.writer(opened_file, delimiter=',')
        writer.writerows(rows)


def get_fio(text):
    res = re.findall(r"[А-Я][а-я]+", text)
    return res


def get_phone(text):
    if not text:
        return text
    number_by_groups = re.match(r"(\+7|8)\s*\D*\(*(\d{3,5})\)*\s*\D*(\d{3})\D*(\d{2})\D*(\d{2})\s*\D*(\d*)", text)
    res = f"{'+7' if number_by_groups.group(1) == '+7' else '8'}({number_by_groups.group(2)})" \
          f"{number_by_groups.group(3)}-" \
          f"{number_by_groups.group(4)}-" \
          f"{number_by_groups.group(5)}{' доб. '+ number_by_groups.group(6) if number_by_groups.group(6) else ''}"

    return res


if __name__ == '__main__':
    base_path = os.path.basename('.')
    path_to_data = os.path.join(base_path, 'phonebook_raw.csv')
    phone_data = read_csv_data(path_to_data)[1:]

    new_phone_data = {}
    for row in phone_data:
        fio = get_fio(" ".join(row[0:3]))
        lastname = fio[0]
        my_dict = {'ФИО': fio, 'Организация': row[3],
                   'Должность': row[4], 'Телефон': get_phone(row[5]), 'Email': row[6]}

        if lastname not in new_phone_data:
            new_phone_data[lastname] = my_dict
        else:
            for key, new_val in my_dict.items():
                old_val = new_phone_data[lastname][key]
                if len(str(old_val)) < len(str(new_val)):
                    new_phone_data[lastname][key] = new_val

    new_phone_data_list = list(new_phone_data.values())
    save_new_csv_data(os.path.join(base_path, 'book.csv'), new_phone_data_list)
