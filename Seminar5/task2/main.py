# 28.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Создайте программу для игры в ""Крестики-нолики"".

from func_lib import *

field =[['*','*','*'],
        ['*','*','*'],
        ['*','*','*']]

is_winner_x = False
is_winner_o = False
full_field = False

while not full_field:
    show_field(field)

    point = input('Player X move: ').split()
    
    point_to_field(point, field,'X')
    is_winner_x = check_winner(field,'X')
    full_field = check_full_field(field)

    show_field(field)

    if is_winner_x or full_field:
        break

    point = input('Player O move: ').split()
    
    point_to_field(point,field,'O')
    is_winner_o = check_winner(field,'O')
    full_field = check_full_field(field)

    if is_winner_o:
        break

if is_winner_o:
    print('Player O wins')
elif is_winner_x:
    print('Player X wins')
else:
    print('Draw')
