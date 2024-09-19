def test_vacansies_(test_vacansies):
    assert test_vacansies.name == "Python Developer"
    assert test_vacansies.salary == "100 000-150 000 руб."
    assert test_vacansies.url == "<https://hh.ru/vacancy/123456>"
    assert test_vacansies.description == "Требования: опыт работы от 3 лет..."


def test_validate_salary(test_validate):
    assert test_validate.salary == '0'


def test_ge(test_vacansies, test_validate):
    assert test_vacansies.__ge__(test_validate) is True


def test_cast_to_object():
    pass
