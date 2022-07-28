# 27.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) (доп) Подумайте как наделить бота ""интеллектом""

from Player import *
from func_lib import *
from Pot import *

print('Sweets game. The one who takes the last portion of sweets' \
     +' becomes a winner.')

pot = Pot(21)
Player.MAX_TAKE = 4
Player.pl_pot = pot

player_one = Human_Being('Me')

print('The second player is human or a robot? Enter h - human, r - robot')
choice = input()
if choice == 'h':
     player_two = Human_Being('Him\her')
elif choice == 'r':
     player_two = Bot('Terminator')
else:
     print('Wrong input provided!')
     exit()

while True:
     is_pl_2_move = False
     show_stat(pot.get_pl_1_sweets(),pot.get_pl_2_sweets()
               ,player_one.player_name(),player_two.player_name()
               ,pot.sweets_left)

     print(f"\n{player_one.player_name()}'s move: ",end='')
     take = player_one.take_sweets()
     pot.out(take,is_pl_2_move)

     if pot.sweets_left <= 0:
          break
     
     is_pl_2_move = True
     show_stat(pot.get_pl_1_sweets(),pot.get_pl_2_sweets()
               ,player_one.player_name(),player_two.player_name()
               ,pot.sweets_left)

     print(f"\n{player_two.player_name()}'s move: ",end='')
     take = player_two.take_sweets()
     pot.out(take, is_pl_2_move)

     if pot.sweets_left <= 0:
          break

if is_pl_2_move:
     print(f'\n{player_two.player_name()} wins')
else:
     print(f'\n{player_one.player_name()} wins')
