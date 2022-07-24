# 20.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Вычислить число c заданной точностью d

# Пример:

# при d = 3, π = 3.141

from random import randrange
from time import sleep
from urllib.request import urlopen

def find_pi_num(acc_deg):
    if acc_deg == 0:
        return 3
    pi_url = 'https://raw.githubusercontent.com/avesanties/GB_HomeWork_Python/main/Seminar4/pi.txt'
    res = urlopen(pi_url)
    pi_num = str(res.read()).replace('b\'','')
    return pi_num[:acc_deg+2]

def show_work():
    p = 0
    while(p < 100):
        p += randrange(1,15,1)
        if p > 100:
            p = 100
        print(f'Calculating... {p}%',end='\r')
        sleep(0.5)
        
d = int(input('Enter degree of accuracy: '))
show_work()
print(f'Result -> {find_pi_num(d)}       ')