# 20.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Задайте натуральное число N. Напишите программу,
# которая составит список простых делителей числа N. (1 - составное число)

def find_factors(main_num):
    num = main_num // 2

    def sieve_of_Eratosthenes(num):
        # Список из элементов типа bool
        # Индекс списка соответствует числу
        # Список инициализируем значением True, начиная с индекса 2
        factors_sieve = [bool(f) for f in range(num)]
        factors_sieve[:0] = [False]

        # Оптимизированное через квадраты решето Эратосфена из Wiki
        i = 2
        while(i**2 < num):
            if factors_sieve[i]:
                k = 0
                while(i**2 + k * i < num):
                    factors_sieve[i**2 + k * i] = False
                    k += 1
            i += 1
        return factors_sieve

    factors_prime = sieve_of_Eratosthenes(num)
    res_factors = []
    for j in range(len(factors_prime)):
        if factors_prime[j] and main_num % j == 0:
            res_factors.append(j)
    
    return res_factors

N = 13*17*19*3*2

print(find_factors(N))