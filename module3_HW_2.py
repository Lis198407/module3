# Module 3
# HW 2
"""
Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


Рекомендації для виконання:
Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.
"""

import random
def get_numbers_ticket(min:int, max:int ,quantity:int) -> list:
    lot_numb = list()
    for i in range(min,max):
        lot_numb.append(i)
    lot_choices = random.sample(lot_numb,k=quantity)
    return lot_choices

incur_input = True
while incur_input:
    try:
        min_str, max_str, quantity_str = input("Input min, max and qty: ").split()
        min_val = int(min_str)
        max_val = int(max_str)
        quantity = int(quantity_str)  
        if 1<=min_val<max_val and max_val <=1000 and quantity> 0 and quantity<=(max_val-min_val):
            incur_input = False
        else: 
            raise ValueError
    except ValueError:
        print("Incorect data input. Use positive integer numbers, min should be less than max, quantity more than 0")
        incur_input = True

lottery_numbers = get_numbers_ticket(min_val,max_val,quantity)
print(f"Your numbers is: {lottery_numbers}")