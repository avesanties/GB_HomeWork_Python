# 17.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def neg_fib(n):
    def help_fun(res,n):
        if n == 1:
            return res
        else:
            res.append(res[-1] + res[-2])
            res.insert(0,res[0] + res[1])
            return help_fun(res, n - 1)
    
    return help_fun([-1,0,1],n)

n = 8
print(neg_fib(n))