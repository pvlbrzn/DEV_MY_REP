import threading
import multiprocessing
from task_2 import timer, separator

number = 100000000
THREADS = 4  # Количество потоков
PROCESSES = 4  # Количество процессов


# 1. Обычное однопоточное решение
@separator
@timer
def find_usually_sum():
    total_sum = sum(range(1, number + 1))
    print(f"(Обычный) Сумма: {total_sum}")


# 2. Многопоточный способ
def thread_partial_sum(start, end, result_list, index):
    result_list[index] = sum(range(start, end + 1))


@separator
@timer
def find_thread_sum():
    part_of_nuber = number // THREADS
    threads = []
    results = [0] * THREADS

    for i in range(THREADS):
        start = i * part_of_nuber + 1
        end = (i + 1) * part_of_nuber if i != THREADS - 1 else number
        thread = threading.Thread(target=thread_partial_sum, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)

    print(f"(Потоки) Сумма: {total_sum}")


# 3. Мультипроцессорный способ
def process_partial_sum(start, end, queue):
    queue.put(sum(range(start, end + 1)))


@separator
@timer
def find_processed_sum():
    part_of_number = number // PROCESSES
    processes = []
    queue = multiprocessing.Queue()

    for i in range(PROCESSES):
        start = i * part_of_number + 1
        end = (i + 1) * part_of_number if i != PROCESSES - 1 else number
        process = multiprocessing.Process(target=process_partial_sum, args=(start, end, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = sum(queue.get() for _ in range(PROCESSES))

    print(f"(Процессы) Сумма: {total_sum}")


if __name__ == "__main__":
    find_usually_sum()  # Обычный расчёт
    find_thread_sum()  # Потоковый расчёт
    find_processed_sum()  # Процессный расчёт
