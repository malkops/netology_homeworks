def main():
    try:
        operation, first_num, second_num = input('Введите выражение: ').split()
    except ValueError as e:
        print(f'Было введено больше одной цифры ({e})')
        return None

    assert operation in ['*', '+', '-', '/'], ('Неизвестная операция')

    first_num = float(first_num)
    second_num = float(second_num)

    try:
        if operation == '+':
            print(f'Результат: {first_num + second_num}')
        elif operation == '-':
            print(f'Результат: {first_num - second_num}')
        elif operation == '*':
            print(f'Результат: {first_num * second_num}')
        elif operation == '/':
            print(f'Результат: {first_num / second_num}')
    except ZeroDivisionError as e:
        print(f'Деление на ноль запрещено ({e})')
        return None
    except ValueError as e:
        print(f'Была введена не цифра ({e})')
        return None


main()
