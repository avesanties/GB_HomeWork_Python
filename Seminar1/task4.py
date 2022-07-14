# 14.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая принимает на вход
# координаты двух точек и находит расстояние
# между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
from random import randrange

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def find_distance(point_1 : Point, point_2 : Point):
    return round(math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y)),2)

p_a = Point(randrange(1,10,1),randrange(1,10,1))
p_b = Point(randrange(1,10,1),randrange(1,10,1))

print(f'A({p_a.x},{p_a.y}); B({p_b.x},{p_b.y}) -> {find_distance(p_a,p_b)}')