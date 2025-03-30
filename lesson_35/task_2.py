import time
import requests
import threading
import multiprocessing
from bs4 import BeautifulSoup

# URL для парсинга новостей
URLS = {
    "Habr": "https://habr.com/ru/news/",
    "Reddit": "https://www.reddit.com/r/news/top/"
}

HEADERS = {"User-Agent": "Mozilla/5.0"}


def timer(func):
    """
    Декоратор для таймера
    """

    def inner(*args, **kwargs):
        start_time = time.time()
        result = func()
        end_time = time.time() - start_time
        print(f'Время выполнения функции {func.__name__} = {end_time:.2f} секунд')
        return result

    return inner


def separator(func):
    """
    Декоратор для красивого разделения способов
    """
    def inner(*args, **kwargs):
        print('-' * 200)
        result = func()
        print('-' * 200)
        return result

    return inner


def fetch_headlines(name, url):
    """
    Функция для парсинга перечня сайтов
    """
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return f"[{name}] Ошибка {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    if name == "Habr":
        headlines = [h.text.strip() for h in soup.select("a.tm-title__link")]
    elif name == "Reddit":
        headlines = [h.text.strip() for h in soup.select("h3")]

    headlines = [h.replace("\xa0", " ") for h in headlines if h]

    return f"[{name}] {headlines[:2]}"  # Выводим первые 2 заголовка


# 1. Обычный запрос
@separator
@timer
def default_requests():
    results = [fetch_headlines(name, url) for name, url in URLS.items()]
    for result in results:
        print(result)


# 2. Поточный способ
def threaded_fetch(name, url, results, index):
    results[index] = fetch_headlines(name, url)


@separator
@timer
def threaded_requests():
    threads = []
    results = [None] * len(URLS)

    for i, (name, url) in enumerate(URLS.items()):
        thread = threading.Thread(target=threaded_fetch, args=(name, url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for result in results:
        print(result)


# 3. Процессный способ
def process_fetch(name, url, queue):
    queue.put(fetch_headlines(name, url))


@separator
@timer
def processed_requests():
    processes = []
    queue = multiprocessing.Queue()

    for name, url in URLS.items():
        process = multiprocessing.Process(target=process_fetch, args=(name, url, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = [queue.get() for _ in range(len(URLS))]

    for result in results:
        print(result)


if __name__ == "__main__":
    default_requests()  # Обычный способ
    threaded_requests()  # Потоковый способ
    processed_requests()  # Процессный способ
