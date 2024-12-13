from task_1 import Warehouse, Product


def main():
    my_warehouse = Warehouse()
    my_warehouse.load_from_file("warehouse.json")

    while True:
        print("\nМой склад!")
        print("1. Показать товары на складе")
        print("2. Добавить товар на склад")
        print("3. Найти товар по ID")
        print("4. Найти товар по названию")
        print("5. Сортировать товары по названию")
        print("6. Сортировать товары по магазину")
        print("7. Сортировать товары по цене")
        print("8. Сортировать по ID товара")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            print(my_warehouse.list_products())

        elif choice == "2":
            try:
                name = input("Введите название товара: ")
                store = input("Введите магазин товара: ")
                cost = float(input("Введите цену товара в рублях: "))
                my_warehouse.add_prod(Product(name, store, cost))
                print("Товар добавлен.")
            except ValueError:
                print("Ошибка ввода")

        elif choice == "3":
            prod_id = int(input("Введите ID товара: "))
            print(my_warehouse.get_prod_by_index(prod_id))

        elif choice == "4":
            name = input("Введите название товара: ")
            print(my_warehouse.get_prod_by_name(name))

        elif choice == "5":
            my_warehouse.sort_by_name()
            print("Товары на складе отсортированы по названию")
            print(my_warehouse.list_products())

        elif choice == "6":
            my_warehouse.sort_by_store()
            print("Товары на складе отсортированы по магазину")
            print(my_warehouse.list_products())

        elif choice == "7":
            my_warehouse.sort_by_cost()
            print("Товары на складе отсортированы по цене")
            print(my_warehouse.list_products())

        elif choice == "8":
            my_warehouse.sort_by_id()
            print("Товары на складе отсортированы по ID")
            print(my_warehouse.list_products())

        elif choice == "9":
            my_warehouse.save_to_file('warehouse.json')
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
