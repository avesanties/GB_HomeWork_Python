# 17.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной 
# позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
# ответ: 12

def calc_odd_sum(seq):
    sum = 0
    for i in range(len(seq)):
        if i % 2 != 0:
            sum += seq[i]
    return sum

seq = [2, 3, 5, 9, 3, 4]

print(f'{seq} -> {calc_odd_sum(seq)}')