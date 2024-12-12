"""
Напишите программу с классом Math. При
инициализации атрибутов нет. Реализовать методы addition,
subtraction, multiplication и division. При передаче в методы
двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
"""


class Math:

    @staticmethod
    def addition(num_a, num_b):
        print(f"Сумма чисел {num_a} и {num_b} равна {num_a + num_b}")

    @staticmethod
    def subtraction(num_a, num_b):
        print(f"Разность чисел {num_a} и {num_b} равна {num_a - num_b}")

    @staticmethod
    def multiplication(num_a, num_b):
        print(f"Произведение чисел {num_a} и {num_b} равно {num_a * num_b}")

    @staticmethod
    def division(num_a, num_b):
        try:
            print(f"Результат деления числа {num_a} на число {num_b} "
                  f"равен {num_a / num_b}")
        except ZeroDivisionError:
            print("Деление на ноль не доступно")


Math.addition(2.2, -5)
Math.subtraction(100, 0)
Math.multiplication(12, 13)
Math.division(16, 8)
Math.division(3, 0)
