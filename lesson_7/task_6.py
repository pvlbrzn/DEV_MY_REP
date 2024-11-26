def check_data(inner_func):
    """Декоратор проверяет зарегистрирован ли пользователь"""
    def output_func(user_name):
        user_name_list = ['Pavel', 'User123', 'Vlad', 'Миша', 'Серега']
        if user_name in user_name_list:
            res = inner_func(user_name)
            return res
        else:
            print('Вы не зарегистрированы в нашей сети')

    return output_func


@check_data
def open_user_account(name: str):
    print(f'Привет {name},  вы успешно вошли в ваш аккаунт!')


user = str(input('Введите ваше имя: '))
open_user_account(user)
