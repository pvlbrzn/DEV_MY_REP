"""
 Класс «Товар» содержит следующие закрытые поля:
 ● название товара
 ● название магазина, в котором подаётся товар
 ● стоимость товара в рублях
 Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
 ● вывод информации о товаре со склада по индексу
 ● вывод информации о товаре со склада по имени товара
 ● сортировка товаров по названию, по магазину и по цене
 ● перегруженная операция сложения товаров по цене
"""
import json


class Product:
    prod_id = 0

    def __init__(self, name: str, store: str, cost: float):
        self.__name = name
        self.__store = store
        self.__cost = cost
        self.prod_id = Product.prod_id
        Product.prod_id += 1

    def get_prod_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_cost(self):
        return self.__cost

    def get_id(self):
        return self.prod_id

    def __add__(self, second_prod):
        if isinstance(second_prod, Product):
            return self.__cost + second_prod.__cost
        raise TypeError("Сложение возможно только между объектами класса Product")

    def __str__(self):
        return (f'Товар: "{self.__name}", стоимость: "{self.__cost:.2f} рублей" '
                f'магазин: "{self.__store}", ID - "{self.prod_id}"')


class Warehouse:

    def __init__(self):
        self.__products = []

    def add_prod(self, product: Product):
        self.__products.append(product)

    def get_prod_by_index(self, product_id):
        for prod in self.__products:
            if prod.prod_id == product_id:
                return str(prod)
        return "Товар с таким индексом не найден"

    def get_prod_by_name(self, product_name):
        for prod in self.__products:
            if prod.get_prod_name().lower() == product_name.lower():
                return str(prod)
        return "Товар с таким названием не найден"

    def sort_by_name(self):
        self.__products.sort(key=lambda prod: prod.get_prod_name().lower())

    def sort_by_store(self):
        self.__products.sort(key=lambda prod: prod.get_store().lower())

    def sort_by_cost(self):
        self.__products.sort(key=lambda prod: prod.get_cost())

    def sort_by_id(self):
        self.__products.sort(key=lambda prod: prod.get_id())

    def list_products(self):
        if self.__products:
            return "\n".join(str(prod) for prod in self.__products)
        return 'Товаров на складе нет'

    def save_to_file(self, filename):
        with open(filename, 'w', encoding="utf-8") as json_file:
            data = [prod.__dict__ for prod in self.__products]
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.__products = []
                for prod_data in data:
                    prod = Product(prod_data['_Product__name'], prod_data['_Product__store'],
                                   prod_data['_Product__cost'])
                    prod.prod_id = prod_data['prod_id']
                    self.__products.append(prod)
        except FileNotFoundError:
            pass
