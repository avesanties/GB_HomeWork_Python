# 20.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Задана натуральная степень k. 
# Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) 
# многочлена и вывести на экран.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

superscript_store = {
    "1": "", "2": "²", "3": "³", "4": "⁴"
    , "5": "⁵", "6": "⁶","7": "⁷", "8": "⁸", "9": "⁹"}

from random import randrange

k = 5

factors = [randrange(0,100,1) for x in range(k+1)]

result = ''
for i in range(len(factors)-1,0,-1):
    if factors[i] != 0:
        result += f'{factors[i]}*x{superscript_store.get(str(i))} + '
result += str(factors[-1]) + ' = 0'
print(result)