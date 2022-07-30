# 30.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

values = [1, 23, 42, 'asdfg']

transformation = lambda x: x

transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')