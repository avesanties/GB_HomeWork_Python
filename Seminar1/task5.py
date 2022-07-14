# 14.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from random import randrange

def generate_values():
   return [randrange(0,2,1),randrange(0,2,1),randrange(0,2,1)]

def check_statment(xyz):
    return not (xyz[0] or xyz[1] or xyz[2]) == (not xyz[0]) and (not (xyz[1])) and (not xyz[2])

print(check_statment(generate_values()))
