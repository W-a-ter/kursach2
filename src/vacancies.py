class Vacansies:
    result_list = []
    def __init__(self, name, salary, url, description):
        self.name = name
        self.salary = 0
        self.validate_salary(salary)
        self.url = url
        self.description = description
        vacansies_dict = {
            'name': name,
            'salary': salary,
            'url': url,
            'description': description}
        Vacansies.result_list.append(vacansies_dict)

    def validate_salary(self, salary):
        if salary == 'null':
            self.salary = 0
        else:
            self.salary = salary

    def __ge__(self, other):
        return self.salary >= other.salary

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list):
        for i in hh_vacancies:
            if type(i['area'].get('salary', {'salary': {'from': 0,
                                             'to': 0}})) is dict:
                new_str = ''
                new_str += i['area']['salary']['from']
                new_str += ' - '
                new_str += i['area']['salary']['to']
                i['area']['salary'] = new_str
            list_class = cls(
                name=i['name'],
                salary=i['area'].get('salary', '0'),
                url=i['area']['url'],
                description=i['snippet']['requirement']
            )
            dict_class = {'name': list_class.name,
                          'salary': list_class.salary,
                          'url': list_class.url,
                          'description': list_class.description
                          }
            cls.result_list.append(dict_class)








if __name__ == "__main__":
    vacancy = Vacansies("Python Developer", "100 000-150 000 руб.", "<https://hh.ru/vacancy/123456>",
                      "Требования: опыт работы от 3 лет...")
    print(vacancy.name)