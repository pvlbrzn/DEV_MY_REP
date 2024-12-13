"""
ПчёлоСлон
 Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
 ● fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
 ● trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
 ● eat(meal, value) – может принимать в meal только ”nectar”
или “grass”. Если съедает нектар, то value вычитается из
части слона, пчеле добавляется. Иначе – наоборот. Не
может увеличиваться больше 100 и уменьшаться меньше 0.
"""


class BeeElephant:

    def __init__(self, bee_num: int, ele_num: int):
        self.bee_num = max(0, min(100, bee_num))
        self.ele_num = max(0, min(100, ele_num))

    def fly(self) -> bool:
        """Возвращает True, если часть пчелы не меньше части
        слона, иначе – False"""
        return self.bee_num >= self.ele_num

    def trumpet(self) -> str:
        """
        Eсли часть слона не меньше части пчелы,
        возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
        """
        return "tu-tu-doo-doo" if self.ele_num > self.bee_num else "wzzzzzzzzzz"

    def eat(self, meal: str, value: int):
        if meal not in ("nectar", "grass"):
            raise ValueError("Meal может быть только 'grass' или 'nectar'")

        if meal == "nectar":
            # Пчела увеличивается, слон уменьшается
            self.bee_num = max(0, min(100, self.bee_num + value))
            self.ele_num = max(0, min(100, self.ele_num - value))

        elif meal == "grass":
            # Слон увеличивается, пчела уменьшается
            self.bee_num = max(0, min(100, self.bee_num - value))
            self.ele_num = max(0, min(100, self.ele_num + value))

    def __str__(self):
        return (f"Размер слона - {self.ele_num}, "
                f"размер пчелы - {self.bee_num}")


bee_ele = BeeElephant(10, 15)
print(bee_ele)
print(bee_ele.fly())
print(bee_ele.trumpet())
bee_ele.eat('nectar', 50)
print(bee_ele)
