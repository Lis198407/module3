
# Module 3
# HW 1
"""
Вимоги до завдання:
Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.


Рекомендації для виконання:
Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.
"""

from datetime import datetime

def get_days_from_today(date:datetime)->int:
    current_date = datetime.today()
    return current_date.toordinal()-date.toordinal()

incur_input = True
while incur_input:
    user_date_str = input("Input date as YYYY.MM.DD:  ")
    try:
        user_date = datetime.strptime(user_date_str, "%Y.%m.%d")
        incur_input = False
    except ValueError:
        print("Incorect data input")
        incur_input = True

date_diff = get_days_from_today(user_date)
print(f"Days from today: {date_diff}")