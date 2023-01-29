# Задача №1 Кто самый умный супергерой?

import requests

def intelligence_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    responce = requests.get(url)
    heroes = {}
    for i in responce.json():
        name = i['name']
        if name in ['Hulk', 'Captain America', 'Thanos']:
            character = i['powerstats']
            for key in character.keys():
                if key == 'intelligence':
                    heroes.setdefault(name, character[key])
                    k, v = max((k, v) for k, v in heroes.items())
    print(f"Самый умный супергерой: {k}")

intelligence_heroes()

# Задача №2 Программа, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.

from pprint import pprint

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):                    # Получение ссыдки для загрузки файла на ЯндексДиск
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}     # path где будет лежать файл ("Netology/Задание.txt"), overwrite - перезаписать
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):       # Загрузка файла в ЯндексДиск
        result = self._get_upload_link(disk_file_path=disk_file_path)
        url = result.get("href")                                   # из словаря result получить значение по ключу "href" (лежит ссылка загрузки файла)
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()                                # raise_for_status() возвращает объект HTTPError, если в процессе произошла ошибка
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    ya = YandexDisk(token=" ")
    ya.upload_file_to_disk(disk_file_path="Netology/Задание.txt", filename="ДЗ.txt")


