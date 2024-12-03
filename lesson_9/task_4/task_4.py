"""
Напишите программу, которая получает на вход строку
с названием текстового файла и выводит на экран
содержимое этого файла, заменяя все запрещённые слова
звездочками. Запрещённые слова, разделённые символом
пробела, должны храниться в файле stop_words.txt.
Программа должна находить запрещённые слова в любом месте файла,
даже в середине другого слова.
Замена независима от регистра: если в списке
запрещённых есть слово exam, то замениться должны exam,
eXam, EXAm и другие вариации.
"""


def load_blocked_words(file_path: str) -> set:
    """
    Загружает список запрещённых слов из файла stop_words.txt.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return set(content.strip().lower().split())


def censor_word(word: str, blocked_words: set) -> str:
    """
    Заменяет слово на звёздочки, если оно есть в списке запрещённых слов.
    """
    if word.lower() in blocked_words:
        return '*' * len(word)
    return word


def censor_file(input_file: str, blocked_words: set) -> None:
    """
    Считывает текст из файла, заменяет запрещённые слова на звёздочки
    и выводит результат в консоль.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Заменяем каждое запрещённое слово на звёздочки
    words = content.split()
    censored_words = [censor_word(word, blocked_words) for word in words]
    censored_content = ' '.join(censored_words)

    print(censored_content)


stop_words_file = "stop_words.txt"
input_file_path = "text_file.txt"
stop_words = load_blocked_words(stop_words_file)
censor_file(input_file_path, stop_words)

