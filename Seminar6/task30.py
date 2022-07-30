# 30.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

def same_by(characteristic, objects):
   results = [characteristic(obj) for obj in objects]
   return all([results[0] == res for res in results[1:]])

values = [1,7,3,27]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')