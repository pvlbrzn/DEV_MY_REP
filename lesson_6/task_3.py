from math import sqrt

"""
Программа получает на вход число.
Реализовать функцию, которая определяет, 
является ли это число простым.
"""

while True:
    print("Программа проверяет простое число или нет. "
          "Для выхода из программы введите '0'")
    n = int(input('Введите целое положительное число: '))
    if n == 0:
        print('Вы вышли из программы, хорошего дня!')
        break


    def is_prime(num: int) -> bool:
        """Функция проверяет простое число или нет"""
        if num < 2:
            return True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


    print(f"Число {n} простое" if is_prime(n) is True else f'Число {n} не простое')
