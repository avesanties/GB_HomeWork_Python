# 16.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Задана последовательность натуральных чисел,
# завершающаяся числом 0. Требуется определить
# значение второго по величине элемента в этой
# последовательности, то есть элемента, который
# будет наибольшим, если из последовательности удалить
# наибольший элемент.
# Пример:
# 1
# 7
# 9
# 0
# Вывод:
# 7

def find_2nd_max(seq):
    if(seq[0] > seq[1]):
        max = seq[0]
        max_2nd = seq[1]
    else:
        max = seq[1]
        max_2nd = seq[0]
    for i in range(2,len(seq)):
        if seq[i] > max:
            max_2nd = max
            max = seq[i]
        elif seq[i] > max_2nd and seq[i] < max:
            max_2nd = seq[i]
    return max_2nd

seq = [1,6,8,6,99,1,8,99,45,12,0]

for i in seq:
    print(i)

print('Output:')
print(find_2nd_max(seq))

