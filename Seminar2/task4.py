# 16.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит
# не менее Y рублей.

# Пример:
# 100
# 10
# 200
# Вывод:
# 8
def find_years_qnt(deposit,percent,goal):
    sum = deposit
    count = 0
    while(sum < goal):
        sum += round(sum * percent,2)
        count += 1
    return count

x = 100
p = 10/100
y = 200
print(x)
print(p)
print(y)
print('Output:')
print(find_years_qnt(x,p,y))

