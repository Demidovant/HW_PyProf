from application.salary import *
from application.db.people import *
from datetime import *
from art import *


if __name__ == '__main__':
    print(t := datetime.now().strftime("%Y-%m-%d %H:%M"))
    calculate_salary()
    get_employees()
    tprint(t)