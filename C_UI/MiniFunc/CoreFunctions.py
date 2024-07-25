import os
import json


def write_settings(key, value):
    # Поиск абсолютного пути
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', "Data", "settings.json")

    # Если файла не существует, создаем его
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    # Перезаписываем файл настроек
    data = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)

    # Обновляем значение по ключу
    data[key] = value

    with open(file_path, 'w', encoding='UTF-8') as file:
        json.dump(data, file)


def read_settings(key):
    # Поиск абсолютного пути
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', "Data", "settings.json")

    # Читаем файл настроек
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
            return data.get(key)
    else:
        return None
