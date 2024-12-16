"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2…).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""


def cyclic_sequence(sequence):
    while True:
        for num in sequence:
            yield num


def main():
    sequence = [1, 2, 3]
    count = int(input("Введите количество чисел для вывода: "))

    generator = cyclic_sequence(sequence)
    result = [next(generator) for _ in range(count)]

    print("Результат:", result)


if __name__ == "__main__":
    main()
