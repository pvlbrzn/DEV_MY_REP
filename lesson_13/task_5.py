"""
 Паттерн «Стратегия»
 ● Создайте класс Calculator, который использует разные
стратегии для выполнения математических операций.
 ● Создайте несколько классов, каждый реализует
определенную стратегию математической операции,
например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute, который
принимает два числа и выполняет соответствующую
операцию.
 ● Calculator должен иметь метод set_strategy, который
устанавливает текущую стратегию, и метод calculate,
который выполняет операцию с помощью текущей стратегии.
"""


class Addition:
    def execute(self, num_a, num_b):
        return num_a + num_b


class Subtraction:
    def execute(self, num_a, num_b):
        return num_a - num_b


class Multiplication:
    def execute(self, num_a, num_b):
        return num_a * num_b


class Division:
    def execute(self, num_a, num_b):
        try:
            return num_a / num_b
        except ZeroDivisionError:
            return "Деление на ноль не доступно"


class Calculator:

    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, num_a, num_b):
        if not self.strategy:
            print('НЕ выбрана стратегия')
        else:
            return self.strategy.execute(num_a, num_b)


def main():
    calculator = Calculator()

    calculator.set_strategy(Addition())
    print("Сложение:", calculator.calculate(10, 5))

    calculator.set_strategy(Subtraction())
    print("Вычитание:", calculator.calculate(10, 5))

    calculator.set_strategy(Multiplication())
    print("Умножение:", calculator.calculate(10, 5))

    calculator.set_strategy(Division())
    print("Деление:", calculator.calculate(10, 5))
    print("Деление:", calculator.calculate(10, 0))


if __name__ == "__main__":
    main()

