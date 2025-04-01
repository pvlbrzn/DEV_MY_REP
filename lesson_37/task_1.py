import asyncio
import time


async def download_data():
    print("Начало работы функции")
    await asyncio.sleep(3)
    print('Данные загружены')


async def main():
    task1 = asyncio.create_task(download_data())
    task2 = asyncio.create_task(download_data())

    await task1
    await task2


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter() - start_time
    print(f'{__file__} выполнится за {end_time:.4f} секунд')
