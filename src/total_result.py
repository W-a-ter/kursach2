def filter_vacancies(api_list: list, api_words: list):
    new_list = []
    for k in api_words:
        for i in api_list:
            if k in i.get('name', ' ') or i.get('description', ' '):
                if i not in new_list:
                    new_list.append(i)
                else:
                    continue
    return new_list


def get_vacancies_by_salary(filter_list: list, salary_range: str):
    salary_range_split = salary_range.split(' ')
    total_list = []
    for i in filter_list:
        salary_split = i['salary'].split(' ')
        if salary_range_split[0] >= salary_split[0] and salary_range_split[2] <= salary_split[2]:
            total_list.append(i)
    return total_list
