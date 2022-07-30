# 30.07.2022
# Шлепенков Алексей
# Telegram: @avesanties
# Discord: Alexey Sh.#3490
# e-mail: schlepenkow@gmail.com

vowels = ['а','е','ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

phrases = input('Vinny says: ').split()

phrase_vowels = [list(filter((lambda ch: ch in vowels),phrase)) for phrase in phrases]
result = all([len(phrase_vowels[0]) == len(x) for x in phrase_vowels[1:]])

if result:
    print('Парам пам-пам')
else:
    print('Пам парам')
