class Vacansies:
    def __init__(self, name, salary, url, description):
        self.name = name
        self.salary = 0
        self.validate_salary(salary)
        self.url = url
        self.description = description

    def validate_salary(self, salary):
        if salary == 'null':
            self.salary = 0
        else:
            self.salary = salary

    def __ge__(self, other):
        return self.salary >= other.salary

