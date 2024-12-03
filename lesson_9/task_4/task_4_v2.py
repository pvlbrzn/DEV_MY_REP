def load_blocked_words(file_path: str) -> set:
    """
    Загружает список запрещённых слов из файла stop_words.txt,
    где слова записаны через пробел.

    :param file_path: Путь к файлу с запрещёнными словами.
    :return: Множество запрещённых слов.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return set(content.strip().lower().split())


def censor_text(content: str, blocked_words: set) -> str:
    """
    Заменяет запрещённые слова в тексте на звёздочки, включая их вхождения
    в середину других слов, с учётом регистра.

    :param content: Исходный текст.
    :param blocked_words: Множество запрещённых слов.
    :return: Текст с заменёнными запрещёнными словами.
    """
    censored_content = content
    for word in blocked_words:
        lower_censored_content = censored_content.lower()
        word_len = len(word)
        i = 0
        while i < len(lower_censored_content):
            if lower_censored_content[i:i + word_len] == word:
                # Заменяем подстроку на звёздочки
                censored_content = (
                        censored_content[:i] + '*' * word_len + censored_content[i + word_len:]
                )
                # Обновляем текст в нижнем регистре для продолжения поиска
                lower_censored_content = censored_content.lower()
                i += word_len  # Пропускаем заменённое слово
            else:
                i += 1
    return censored_content


def censor_file(input_file: str, blocked_words: set) -> None:
    """
    Считывает текст из файла, заменяет запрещённые слова на звёздочки
    и выводит результат в консоль.

    :param input_file: Путь к текстовому файлу для обработки.
    :param blocked_words: Множество запрещённых слов.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Заменяем запрещённые слова на звёздочки
    censored_content = censor_text(content, blocked_words)

    # Выводим результат
    print("Цензурированный текст:")
    print(censored_content)


# Пример использования
if __name__ == "__main__":
    stop_words_file = "stop_words.txt"  # Путь к файлу с запрещёнными словами
    input_file_path = "text_file.txt"  # Путь к текстовому файлу для обработки

    try:
        # Загружаем запрещённые слова
        blocked_words = load_blocked_words(stop_words_file)

        # Цензурируем текст из входного файла
        censor_file(input_file_path, blocked_words)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
