from src.Json_saver import JsonSaver


def test_json_saver(test_vacansies, test_json):
    json_saver = JsonSaver('../Data/JsonFile.json')
    json_saver.add_vacancies(test_vacansies.result_list)
    with open('../Data/JsonFile.json', encoding='utf-8') as file:
        assert test_json == file.read()


def test_json_remove(test_vacansies):
    json_saver = JsonSaver('../Data/JsonFile.json')
    #json_saver.add_vacancies(test_vacansies.result_list)
    json_saver.remove_vacancies(test_vacansies)
    with open('../Data/JsonFile.json', encoding='utf-8') as file:
        assert '[]' == file.read()
