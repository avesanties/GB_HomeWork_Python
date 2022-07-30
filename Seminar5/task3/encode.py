# 28.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Реализуйте RLE алгоритм: реализуйте 
# модуль сжатия и восстановления данных.


input = '55555'
output = ''
buff = ''
count = 0
for i in range(len(input)):
    count += 1
    buff += input[i]
    if not (i != len(input) - 1 and input[i] == input[i+1]):
        if len(buff) >= 3:
            symbol = chr(count)
            output += f'#{symbol}{buff[0]}'
        else:
            output += buff

        count = 0
        buff = ''

with open('output','w') as fl:
    fl.write(output)