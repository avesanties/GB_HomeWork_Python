# 30.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

import math


def find_farthest_orbit(orbits):
    squares = [x * y * math.pi for (x,y) in orbits]
    return orbits[squares.index(max(squares))]

    
orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
print(*find_farthest_orbit(orbits))