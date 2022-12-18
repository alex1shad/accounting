from pprint import pprint
from datetime import date
from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from pypi_test.vk_pypi import get_info


if __name__ == '__main__':
    date_now = date.today()
    print(date_now)
    cs()
    ge()
    print()
    user_ids = input('Введите id пользователей\n')
    pprint(get_info(user_ids))
