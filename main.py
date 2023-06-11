from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from art import tprint


if __name__ == '__main__':
    print(t := datetime.now().strftime("%Y-%m-%d %H:%M"))
    calculate_salary()
    get_employees()
    tprint(t)
