"""
Разработать класс SuperStr, который наследует функциональность стандартного
типа str и содержит два новых метода:
● метод is_repeatance(s), который принимает некоторую строку и возвращает
True или False в зависимости от того, может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая строка не содержит повторов;
● метод is_palindrom(), который возвращает True или False в зависимости от того,
является ли строка палиндромом вне зависимости от регистра. Пустую строку считать
палиндромом.
"""


class SuperStr(str):

    def is_repeatance(self, s: str) -> bool:
        """
        Проверяет можно ли получить строку целым числом
        повторов принимаемой строки 's'
        """
        if not s:
            return False
        return len(self) % len(s) == 0 and self == s * (len(self) // len(s))

    def is_palindrom(self) -> bool:
        """Функция проверяет, является ли строка палиндромом."""
        if not self:  # Если строка пустая
            return True
        low_str = self.lower()  # перевод строки в нижний регистр
        return low_str == low_str[::-1]


s1 = SuperStr("ahahahahah")
print(s1.is_repeatance("ah"))  # True
print(s1.is_repeatance("aha"))  # False
print(s1.is_repeatance(''))  # False

# Палиндром -> True
s2 = SuperStr("radar")
print(s2.is_palindrom())

# Не палиндром -> False
s3 = SuperStr("hello")
print(s3.is_palindrom())

# Пустая строка -> True
s4 = SuperStr('')
print(s4.is_palindrom())
