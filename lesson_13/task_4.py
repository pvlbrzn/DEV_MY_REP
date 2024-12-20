"""
 Паттерн «Фабричный метод»
 ● Создайте абстрактный класс Animal, у которого есть
абстрактный метод speak.
 ● Создайте классы Dog и Cat, которые наследуют от Animal
 и реализуют метод speak.
 ● Создайте класс AnimalFactory, который использует
паттерн «Фабричный метод» для создания экземпляра
Animal. Этот класс должен иметь метод create_animal,
который принимает строку («dog» или «cat») и возвращает
соответствующий объект (Dog или Cat).
"""
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        return 'Гав-Гав'


class Cat(Animal):
    def voice(self):
        return 'Мяу-мяу'


class AnimalFactory:

    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


def main():
    factory = AnimalFactory()

    dog = factory.create_animal("dog")
    print(f"Собака издает звук: {dog.voice()}")

    cat = factory.create_animal("cat")
    print(f"Кошка издает звук: {cat.voice()}")

    try:
        animal = factory.create_animal("Корова")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
