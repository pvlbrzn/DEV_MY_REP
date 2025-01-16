from collections import deque


graph = {}
graph["вы"] = ["Алиса", "Боб", "Клэр"]
graph["Боб"] = ["Анудж", "Пегги"]
graph["Алиса"] = ["Пегги"]
graph["Клэр"] = ["Том", "Джонни"]
graph["Анудж"] = []
graph["Пегги"] = []
graph["Том"] = []
graph["Джонни"] = []


def search(name):
    search_queue = deque()  # Создание новой очереди
    search_queue += graph[name]  # Все соседи добавляются в очередь поиска
    searched = set()  # Этот массив используется для отслеживания уже проверенных людей
    while search_queue:  # Цикл пока очередь не пуста
        person = search_queue.popleft()  # Из очереди извлекается первый человек
        if not person in searched:  # Проверяем только в том случае, если он не проверялся ранее
            if person_is_seller(person):  # Проверяем является ли человек продавцом
                print(person + ' продавец!')
                return True
            else:
                search_queue += graph[person]  # Если не является - все друзья человека добавляются в очередь
                searched.add(person)  # Человек помечается как уже проверенный.
    return False  # Если выполнение дошло сюда - значит в очереди нет продавца.


def person_is_seller(name):
    return name[-1] == 'м'


search('вы')

