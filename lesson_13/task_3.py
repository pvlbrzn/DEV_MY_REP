"""
Паттерн «Строитель»
 ● Создайте класс Pizza, который содержит следующие атрибуты:
 size, cheese, pepperoni, mushrooms, onions, bacon.
 ● Создайте класс PizzaBuilder, который использует паттерн «Строитель»
 для создания экземпляра Pizza. Этот класс должен содержать методы для
 добавления каждого из атрибутов Pizza.
 ● Создайте класс PizzaDirector, который принимает экземпляр PizzaBuilder
 и содержит метод make_pizza, который использует PizzaBuilder для создания Pizza
"""


class Pizza:

    def __init__(self, size, cheese=False, pepper=False, mushroom=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepper = pepper
        self.mushroom = mushroom
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("сыр")
        if self.pepper:
            toppings.append("пепперони")
        if self.mushroom:
            toppings.append("грибы")
        if self.onions:
            toppings.append("лук")
        if self.bacon:
            toppings.append("бекон")
        toppings_str = ", ".join(toppings) if toppings else "без добавок"
        return f"Пицца {self.size} см с добавками {toppings_str}"


class PizzaBuilder:

    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepper = False
        self.mushroom = False
        self.onions = False
        self.bacon = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepper(self):
        self.pepper = True
        return self

    def add_mushroom(self):
        self.mushroom = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepper, self.mushroom, self.onions, self.bacon)


class PizzaDirector:

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, with_cheese=False, with_pepper=False, with_mushroom=False,
                   with_onions=False, with_bacon=False):
        if with_cheese:
            self.builder.add_cheese()
        if with_pepper:
            self.builder.add_pepper()
        if with_mushroom:
            self.builder.add_mushroom()
        if with_onions:
            self.builder.add_onions()
        if with_bacon:
            self.builder.add_bacon()

        return self.builder.build()


def main():
    print("Создаём пиццу через Builder и Director!")

    pizza_builder = PizzaBuilder(size=30)
    director = PizzaDirector(pizza_builder)
    pizza = director.make_pizza(with_cheese=True, with_pepper=True, with_bacon=True)
    print(pizza)

    print("\nСоздаём другую пиццу напрямую через Builder!")
    another_pizza = PizzaBuilder(size=25).add_mushroom().add_onions().build()
    print(another_pizza)


if __name__ == "__main__":
    main()
