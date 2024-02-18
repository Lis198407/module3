# Module 3
# HW 4

"""
Вимоги до завдання:
Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


Рекомендації для виконання:
Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
Визначте поточну дату системи за допомогою datetime.today().date().
Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.

"""

from datetime import datetime

now = datetime.now()
def get_upcoming_birthdays(users:list) ->list:
    date_diff = 0
    i=0
    user_dict = {}
    upcoming_birth_list=[]
    for usr_dict in users:
        user_dict = users[i]
        try:
            birthday_datetime = datetime.strptime(user_dict.get("birthday"),"%Y.%m.%d")
            greeting_date = birthday_datetime.replace(year = now.year)                                                            #changing the year to current
            datediff = greeting_date.day-now.day                                                                                  #difference between today and birthday date
            if datediff in range(0,7):                                                                                            #if less than 7 days than - add to list 
                if greeting_date.weekday() in [5,6]: 
                    greeting_date = datetime(greeting_date.year,greeting_date.month,greeting_date.day+7-greeting_date.weekday())  # shift to next monday if weekend
                upcoming_birth_list.append({"user": user_dict.get("name"), "greeting_date": greeting_date.strftime("%Y.%m.%d")})  # add to list
        except Exception as mes:
            print(f"Error in date {user_dict.get("name")}: {user_dict.get("birthday")}. error message {mes}") 
        i +=1
    return upcoming_birth_list

users = [
    {"name": "John Doe", "birthday": "1985.02.23"},
    {"name": "Jane Smith", "birthday": "1990.02.27"},
    {"name": "John Doe2", "birthday": "1985.02.10"},
    {"name": "Jane Smith2", "birthday": "1990.02.11"},
    {"name": "John Doe3", "birthday": "1985.02.08"},
    {"name": "Jane Smith2", "birthday": "1990.02.15"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)