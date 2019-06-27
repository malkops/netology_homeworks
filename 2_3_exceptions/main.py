def main():
    try:
        operation, first_num, second_num = input('Введите выражение: ').split()
    except ValueError as e:
        return f'Было введено больше одной цифры ({e})'

    assert operation in ['*', '+', '-', '/'], ('Неизвестная операция')

    try:
        first_num = float(first_num)
        second_num = float(second_num)
    except ValueError as e:
        return f'Были введены не цифры ({e})'

    try:
        if operation == '+':
            result = first_num + second_num
        elif operation == '-':
            result = first_num - second_num
        elif operation == '*':
            result = first_num * second_num
        elif operation == '/':
            result = first_num / second_num
    except ZeroDivisionError as e:
        return f'Деление на ноль запрещено ({e})'
    except ValueError as e:
        return f'Была введена не цифра ({e})'

    return f'Результат: {result}'


main()
