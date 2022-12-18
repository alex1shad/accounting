from pprint import *
from datetime import *
from application.salary import *
from application.db.people import *
from pypi_test.vk_pypi import *


if __name__ == '__main__':
    date_now = date.today()
    print(date_now)
    calculate_salary()
    get_employees()
    print()
    user_ids = input('Ввведите id пользователей:\n')
    pprint(get_info(user_ids))
