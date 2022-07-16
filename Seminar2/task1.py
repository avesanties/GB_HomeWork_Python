# 16.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def calc_digits_sum(num_str):
    num_str = num_str.replace('.','')
    sum = 0
    for i in num_str:
        sum += int(i)
    return sum

num = input('Enter real num: ')
print(f'{num} -> {calc_digits_sum(num)}')