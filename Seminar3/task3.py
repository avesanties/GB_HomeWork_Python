# 17.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной 
# части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_max_min_fraction_diff(seq):
    def frac(num):
        frac = num - int(num)
        if frac > 0:
            return round(frac,3)
        else: 
            return -1
    
    fracs = []
    for i in seq:
        fracs.append(frac(i))

    if fracs[0] > fracs[1]:
        max_frac = fracs[0]
        min_frac = fracs[1]
    else:
        max_frac = fracs[1]
        min_frac = fracs[0]
    
    for i in range(2,len(fracs)):
        if fracs[i] == -1:
            continue

        if fracs[i] > max_frac:
            max_frac = fracs[i]
        if fracs[i] < min_frac:
            min_frac = fracs[i]
    
    return round(max_frac - min_frac,3)

seq = [1.1, 1.2, 3.1, 5, 10.01]
print(f'{seq} => {find_max_min_fraction_diff(seq)}')