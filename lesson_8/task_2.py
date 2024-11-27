"""
Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку
исключений.
"""

try:
    def primitive_calc(a: float, b: float, action: str):
        """Примитивный калькулятор на 4 операции"""
        if action == '+':
            print(a + b)
        elif action == '-':
            print(a - b)
        elif action == '*':
            print(a * b)
        elif action == '/':
            print(a / b)
        else:
            print('Операция не поддерживается')


    num_1 = float(input("Введите первое число: "))
    operation = str(input('Что нужно сделать ("+", "-", "*", "/"): '))
    num_2 = float(input("Введите второе число: "))
    primitive_calc(num_1, num_2, operation)

except (TypeError, ValueError):
    print("Не верный ввод")
except (ZeroDivisionError):
    print("На ноль делить нельзя.")
