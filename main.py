from src.hh_api import HH
from src.vacancies import Vacansies
from src.Json_saver import JsonSaver
from src.total_result import filter_vacancies
from src.total_result import get_vacancies_by_salary
# vacancie = Vacansies(' ', ' ', ' ', ' ')
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacansies.cast_to_object_list(hh_api.vacancies)

#Пример работы контструктора класса с одной вакансией
#vacancy = Vacansies("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
# json_saver = JsonSaver()
# json_saver.add_vacancies(vacancy)
# json_saver.remove_vacancies(vacancy)

#Функция для взаимодействия с пользователем


def user_interaction():
    hh_api = HH(' ')
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacansies.cast_to_object_list(hh_api.vacancies)

    filtered_vacancies = filter_vacancies(hh_api.vacancies, filter_words)


    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()