import requests


def get_json(url: str) -> dict:
    """
    Функция скачивает JSON-данные по указанной ссылке.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        return response.json()  # Преобразуем ответ в JSON-формат
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return {}


def save_json_to_file(data: dict, file_path: str) -> None:
    """
    Сохраняет JSON-данные в файл.
    """
    import json
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"JSON-данные сохранены в файл: {file_path}")


some_url = "https://drive.google.com/uc?id=1ehMOo7pP6ZQdX3CRmaba3ljY-hISU33n"
output_file = "data.json"

# Получаем данные из ресурса
json_data = get_json(some_url)
# Сохраняем данные
if json_data:
    save_json_to_file(json_data, output_file)
