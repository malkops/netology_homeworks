try:
    operation, *num = input('Imput operation: ').split()
    assert operation in ['+', '-', '/', '*'], 'Only basic mathematical operations are supported'
    first_num, second_num = map(float, num)
except (ValueError, AssertionError) as err:
    print('Mistakes were made: {err}')
else:
    if operation == '+':
        print(first_num + second_num)
    elif operation == '-':
        print(first_num - second_num)
    elif operation == '*':
        print(first_num*second_num)
    elif operation == '/':
        try:
			print(first_num/second_num)
		except ZeroDivisionError as err:
			print('You got infinity: {err}')



