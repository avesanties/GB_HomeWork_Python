# 09.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

# Пример:

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

def find_quarter(x,y):
    if x == 0:
        return 'Ось X'
    elif y == 0:
        return 'Ось Y'
    
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3

x = int(input('Enter X: '))
y = int(input('Enter Y: '))

print(f'x={x}; y={y} -> {find_quarter(x,y)}')