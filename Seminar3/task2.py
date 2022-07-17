# 17.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Напишите программу, которая найдёт 
# произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def calc_pair_sum(seq):
    def help_fun(n,res):
        if n < len(seq) / 2:
            res.append(seq[n] * seq[len(seq) - 1 - n])
            return help_fun(n+1,res)
        else:
            return res
    return help_fun(0,[])


seq = [2, 3, 5, 6]

print(calc_pair_sum(seq))

# Решение вдохновлено вот этим:
# https://www.coursera.org/learn/programming-languages/home/info
# и вот этим:
# https://stackoverflow.com/questions/30214531/basics-of-recursion-in-python