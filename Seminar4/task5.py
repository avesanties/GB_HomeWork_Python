# 24.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from pathlib import Path
from re import match
from regex import search

def load_polynom(file):
    with open(file,'r') as fl:
        polynom = fl.readline()

    return polynom

def get_factor_from_match(match: match):
    if match:
        if match[0] != '':
            return int(match[0])
        else :
            return 1
    else:
        return -1

def get_factors(polynom):
    factors = []

    for val in superscript_store.values():
        if val == "":
            continue
        match = search('\d*\**x' + val,polynom)
        match = search('\d*(?=\**x' + val + ')',polynom)
        factors.append(get_factor_from_match(match))

    match = search('\d*(?=\**x )',polynom)
    factors[:0] = [get_factor_from_match(match)]

    match = search(' \d* ',polynom)
    factors[:0] = [get_factor_from_match(match)]
    
    return factors

def sum_polynoms(factors_list):
    result = [0 for x in range(len(factors_list[0]))]
    for factors in factors_list:
        for i in range(len(result)):
            if factors[i] != -1:
                result[i] += factors[i]
    
    return result

def make_polynom(factors):
    result = ''
    for i in range(len(factors)-1,0,-1):
        if factors[i] != 0:
            result += f'{str(factors[i]) + "*" if factors[i] != 1 else ""}x{superscript_store.get(str(i))} + '
    result += str(factors[0]) + ' = 0'
    
    return result




superscript_store = {
     "1": "", "2": "²", "3": "³", "4": "⁴"
    , "5": "⁵", "6": "⁶","7": "⁷", "8": "⁸", "9": "⁹"}
polynoms = []

path_to_polynoms = Path('.')
for file in path_to_polynoms.iterdir():
    if '.pol' in file.name:
        polynoms.append(
                        load_polynom(file.name))

factors = []
for pol in polynoms:
    factors.append(get_factors(pol))

res_factors = sum_polynoms(factors)

polynom_str = make_polynom(res_factors)

with open('task5_sum','w') as fl:
    fl.write(polynom_str)