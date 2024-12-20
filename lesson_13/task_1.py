"""
Реализовать программу для вывода
последовательности чисел Фибоначчи до определённого
числа в последовательности. Номер числа, до которого нужно
выводить, задаётся пользователем с клавиатуры. Для
реализации последовательности использовать генераторную
функцию.
"""


def gener_fib_nums(num):
    row = list([0, 1])
    while num > 0:
        new_el = row[-2] + row[-1]
        row.append(new_el)
        yield new_el
        num -= 1


def main():
    try:
        some_num = int(input("Сколько чисел хотите вывести: "))
        for el in gener_fib_nums(some_num):
            print(el, end=' ')
    except ValueError:
        print("Вы ввели что-то не то(((")


if __name__ == "__main__":
    main()


