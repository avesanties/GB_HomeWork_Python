# 16.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая принимает 
# на вход число N и выдает набор произведений 
# чисел от 1 до N. Факториал
# 5! = 120

def factorial_sum(n):
    if n == 1:
        return 1
    else:
        return n * factorial_sum(n-1)

n = int(input('Enter num: '))
print(f'{n} -> {factorial_sum(n)}')