# 14.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек 
# в этой четверти (x и y).

def find_quarter(quarter_num):
    if quarter_num == 1:
        return 'XE(0;inf+) YE(0;inf+)'
    elif quarter_num == 2:
        return 'XE(-inf;0) YE(0;inf+)'
    elif quarter_num == 3:
        return 'XE(-inf;0) YE(-inf;0)'
    elif quarter_num == 4:
        return 'XE(0;inf+) YE(-inf;0)'
    else:
        return 'Quarter not found'

num = int(input("Enter quarter number: "))
print(f'{num} -> {find_quarter(num)}')