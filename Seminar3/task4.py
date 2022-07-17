# 17.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def to_bin(num):
    if num < 2:
        return str(num)
    else:
        return str(to_bin(num // 2)) + str(num % 2)

num = 9
print(f'{num} -> {to_bin(num)}')