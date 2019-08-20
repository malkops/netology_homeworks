import datetime
import pickle


def logger(path):
    def debug(old_function):
        def new_function(*args, **kwargs):
            try:
                with open(path, 'ab+') as file:
                    time_now = datetime.datetime.now()
                    function_name = old_function.__name__
                    result_function = old_function(*args, **kwargs)
                    log_string = f'Time: {time_now}, \nFunction name: {function_name}, ' \
                        f'\nArguments: {args, kwargs}, \nResult: {result_function}\n'
                    pickle.dump(log_string, file)
                    return 'Инфа записана'

            except Exception:
                return 'Что-то пошло не так'
        return new_function
    return debug


@logger('./logger.dat')
def acquaintance(boys, girls):
    if len(boys) != len(girls):
        return 'Никого знакомить не будем - кто-то может остаться без пары'
    result = 'Идеальные пары:\n'
    result += '\n'.join('{0} и {1}'.format(x[0], x[1]) for x in zip(sorted(boys), sorted(girls)))
    return result


if __name__ == '__main__':

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

    acquaintance(boys, girls)

    with open('logger.dat', 'rb') as file:
        while True:
            try:
                print(pickle.load(file))
            except EOFError:
                break
