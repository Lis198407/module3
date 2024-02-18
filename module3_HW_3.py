
# Module 3
# HW 3
"""
Вимоги до завдання:
Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
Функція видаляє всі символи, крім цифр та символу '+'.
Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') та коли номер починається без коду (додається '+38').
Функція повертає нормалізований телефонний номер у вигляді рядка.

Рекомендації для виконання:
Використовуйте модуль re для регулярних виразів для видалення непотрібних символів.
Перевірте, чи номер починається з '+', і виправте префікс згідно з вказівками.
Видаліть всі символи, крім цифр та '+', з номера телефону.
На забувайте повертати нормалізований номер телефону з функції.
"""

import re

def normalize_phone(phone_number:str)->str:
    pattern = r"\D"   # what should be deleted
    normalized_numb = re.sub(pattern,"",phone_number) #removesymbols
    len_norm_nmb = len(normalized_numb)
    match len_norm_nmb:                           #normalize cases
        case 12:
            normalized_numb = "+"+normalized_numb #starts from "+" and have 12 digits then normalize
        case 10:
            normalized_numb = "+3"+normalized_numb #10 digits - add +38
        case 9:
            normalized_numb = "+38"+normalized_numb #9digits - add +380
        case _:
            print(f"number cannot be normilized {phone_number}") #less than 9digit - print - err with number
            normalized_numb = "error "+normalized_numb
    return normalized_numb

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "3'80501234567! asdas",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22dsa $",
    "38050 111 22 11   ",
    " 111 22 11   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)