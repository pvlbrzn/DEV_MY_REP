"""
Класс «Автобус». Класс содержит свойства:
 ● скорость
 ● максимальное количество посадочных мест
 ● максимальная скорость
 ● список фамилий пассажиров
 ● флаг наличия свободных мест
 ● словарь мест в автобусе
 Методы:
 ● посадка и высадка одного или нескольких пассажиров
 ● увеличение и уменьшение скорости на заданное значение
 ● операции in, += и -= (посадка и высадка пассажира по
фамилии)
"""


class Bus:
    def __init__(self, max_speed, max_seats):
        self.speed = 0
        self.max_speed = max_speed
        self.max_seats = max_seats
        self.passengers = []
        self.free_seats = True
        self.seats = {i: None for i in range(1, max_seats + 1)}

    def change_speed(self, operation, set_value):
        """Увеличение или уменьшение скорости на заданное значение."""
        if operation not in ('add_speed', 'remove_speed'):
            raise ValueError("operation может быть только 'add_speed' или 'remove_speed'")

        if operation == 'add_speed':
            new_speed = self.speed + set_value
            if 0 <= new_speed <= self.max_speed:
                self.speed = new_speed
                print(f"Скорость увеличена на {self.speed} км/ч.")
            else:
                print("Невозможно увеличить скорость: превышение предела.")

        elif operation == 'remove_speed':
            new_speed = self.speed - set_value
            if 0 <= new_speed:
                self.speed = new_speed
                print(f"Скорость изменена на {self.speed} км/ч.")
            else:
                print("Невозможно снизить скорость, автобус остановился.")

    def update_free_seats_flag(self):
        """Обновляет флаг наличия свободных мест."""
        if None not in self.seats.values():
            self.free_seats = False

    def board_passenger(self, *last_names):
        """Посадка одного или нескольких пассажиров."""
        for last_name in last_names:
            if not self.free_seats:
                print(f"Нет свободных мест для {last_name}.")
                break
            for seat, human in self.seats.items():
                if human is None:
                    self.seats[seat] = last_name
                    self.passengers.append(last_name)
                    print(f"{last_name} сел(а) на место {seat}.")
                    break
        self.update_free_seats_flag()

    def disembark_passenger(self, *last_names):
        """Высадка одного или нескольких пассажиров."""
        for last_name in last_names:
            if last_name in self.passengers:
                for seat, human in self.seats.items():
                    if human == last_name:
                        self.seats[seat] = None
                        break
                self.passengers.remove(last_name)
                print(f"{last_name} вышел(а) из автобуса.")
            else:
                print(f"{last_name} не найден(а) в автобусе.")
        self.update_free_seats_flag()

    def __contains__(self, last_name):
        """Оператор in: проверяет, находится ли пассажир в автобусе."""
        return last_name in self.passengers

    def __iadd__(self, last_name):
        """Оператор +=: посадка пассажира."""
        self.board_passenger(last_name)
        return self

    def __isub__(self, last_name):
        """Оператор -=: высадка пассажира."""
        self.disembark_passenger(last_name)
        return self

    def __str__(self):
        return (f"Автобус: скорость {self.speed}/{self.max_speed}, "
                f"пассажиры: {', '.join(self.passengers) if self.passengers else 'никого нет'}, "
                f"свободные места: {sum(1 for seat in self.seats.values() if seat is None)}.")


my_bus = Bus(90, 10)

my_bus.board_passenger("Иванов", "Петров", "Сидоров", "Смирнов")
print(my_bus)
print("Иванов" in my_bus)  # True
print("Березан" in my_bus)  # False

my_bus.change_speed('add_speed', 40)
my_bus.change_speed('remove_speed', 20)
my_bus.change_speed('add_speed', 200)  # Невозможно
my_bus.disembark_passenger("Иванов")
print(my_bus)

# Операторы += и -=
my_bus += "Кузнецов"
print(my_bus)
my_bus -= "Петров"
print(my_bus)
