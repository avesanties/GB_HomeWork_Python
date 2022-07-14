# 09.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели,
# и проверяет, является ли этот день выходным.

#Пример:

#- 6 -> да
#- 7 -> да
#- 1 -> нет

def isdayoff (day_num):
    if day_num < 1 or 7 < day_num:
        return "Такого дня нет!"
    elif day_num in {6,7}:
        return 'да'
    else: 
        return 'нет' 

num = int(input("Enter day: "))

print(f'{num} -> {isdayoff(num)}')
