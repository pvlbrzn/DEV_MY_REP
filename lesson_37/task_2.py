import asyncio
import random
import time


async def fetch_data(url):
    download_time = random.randint(1, 3)
    print(f"Загрузка: {url} (ожидание {download_time} сек)")
    await asyncio.sleep(download_time)
    print(f"{url} - успешно загружен")
    return url


async def main(urls_):
    tasks = []
    for url in urls_:
        tasks.append(asyncio.create_task(fetch_data(url)))

    results = await asyncio.gather(*tasks)

    print("\n Результаты:")
    for result in results:
        print(result)


urls = ["https://google.com", "https://habr.com"]

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main(urls))
    end_time = time.perf_counter() - start_time
    print(f'{__file__} выполнится за {end_time:.4f} секунд')

