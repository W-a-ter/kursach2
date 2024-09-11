from src.base_json_saver import BaseJson
import json


class JsonSaver(BaseJson):
    def __init__(self, path_to_file='../Data/JsonFile.json'):
        self.path_to_file = path_to_file
        with open(path_to_file, 'r+', encoding='utf-8') as file:
            self.data = json.load(file)

    def add_vacancies(self, vacancie):
        with open(self.path_to_file, 'r+', encoding='utf-8') as file:
            json.dump(vacancie, file, ensure_ascii=False, indent=4)

    def load_vacancies(self, vacancie: str):
        with open(self.path_to_file, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for i in data:
                if i['name'] == vacancie:
                    print(i)

    def remove_vacancies(self, vacancie):
        new_dict = {
            'name': vacancie.name,
            'url': vacancie.url,
            'salary': vacancie.salary,
            'description': vacancie.description
        }

        with open(self.path_to_file, 'r+', encoding='utf-8') as file:
            data = json.load(file)

        for i in data:
            if i == new_dict:
                data.remove(i)
        with open(self.path_to_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
