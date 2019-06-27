def create_cook_book() -> dict:
    '''
    Преобразовать файл с рецептами в словарь вида:
    {
        "Название блюда": [
            {название ингридиента, количество, мера},
            {название ингридиента, количество, мера}
        ],
        ...
    }
    :return: dict
    '''
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_ingridients = []
            num_ingridients = int(f.readline())
            for i in range(1, num_ingridients+1):
                ing = f.readline().split(' | ')
                dish_ingridients.append({'ingridient_name': ing[0], 'quantity': ing[1], 'measure': ing[2].strip()})
            cook_book[line.strip()] = dish_ingridients
            f.readline()

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    '''
    Возвращает список требуемых ингридиентов,
    с указанием их меры и количества.
    :param dishes: list -- список блюд
    :param person_count: int -- количество гостей
    :return: dict
    '''
    cook_book = create_cook_book()
    needed_ingridients = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingridient_name'] not in needed_ingridients.keys():
                needed_ingridients[ingr['ingridient_name']] = \
                    {'measure': ingr['measure'], 'quantity': int(ingr['quantity'])*person_count}
            else:
                needed_ingridients[ingr['ingridient_name']]['quantity'] += int(ingr['quantity']) * person_count

    return needed_ingridients


def main():
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


if __name__ == '__main__':
    main()
