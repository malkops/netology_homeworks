import textwrap


def adv_print(*args, **kwargs):
    start = kwargs.get('start', '')
    end = kwargs.get('end', '\n')
    max_line = kwargs.get('max_line', 120)
    sep = kwargs.get('sep', ' ')
    file = kwargs.get('in_file', None)
    if max_line > 120:
        max_line = 120
    a = (arg.__str__() for arg in args)
    t = sep.join(a)
    text = textwrap.fill(start + t, width=max_line)
    text += end
    print(text)

    if file:
        with open(file, 'a', encoding='utf-8') as f:
            f.writelines(text)


class PhoneBook:
    def __init__(self, book_name: str):
        self.book_name = book_name
        self.contacts = []

    def print_contacts(self) -> None:
        for contact in self.contacts:
            print(contact)

    def remove_contact(self, phone: "Удаляемый телефон (str)") -> None:
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print(f'Контакт удален:\n{str(contact)}')

    def add_contact(self, contact: object) -> None:
        self.contacts.append(contact)
        print('Контакт добавлен')

    def find_favourite(self) -> list:
        return [contact for contact in self.contacts if contact.favourite]

    def find_contact(self, first_name: str, second_name: str) -> list:
        return [contact for contact in self.contacts
                if contact.first_name == first_name and
                contact.second_name == second_name]


class Contact:
    def __init__(self, first_name: str, second_name: str, phone: str, favourite=False, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.favourite = favourite
        self.addition_information = kwargs

    def __str__(self):
        result_string = f'Имя: {self.first_name}\nФамилия: {self.second_name}\n' \
                        f'Телефон: {self.phone}\nВ избранных: {self.is_favourite()}\n' \
                        f'Дополнительная информация:\n\t{self.addition_information_to_string()}'

        return result_string

    def is_favourite(self) -> str:
        return 'Да' if self.favourite else 'Нет'

    def addition_information_to_string(self) -> str:
        return '\n\t'.join(f'{info}: {value}' for info, value in self.addition_information.items())
