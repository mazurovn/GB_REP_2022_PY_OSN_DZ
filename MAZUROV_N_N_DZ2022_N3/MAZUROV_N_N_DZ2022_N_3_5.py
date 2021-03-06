# Домашнее задание 3 задача 5 Nikolay Mazurov
# ver 2.0 alfa
"""

#  Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из
#  трёх списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
#  (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""


import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number, repeat=False):  #флаг, разрешающий или запрещающий повторы слов в шутках

    jokes = []
    gen_list = min(nouns.copy(),adverbs.copy(),adjectives.copy()) # создаем для генерации

    while number and len(gen_list):
        ver = random.randrange(len(gen_list))
        if repeat:
            jokes.append(f"{nouns.copy().pop(ver)} {adverbs.copy().pop(ver)} {adjectives.copy().pop(ver)}") #проверка повтор
        else:
            jokes.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}") # если нет  генерируется случайный
        number -= 1
    return jokes

print(get_jokes(12, False))
x=input("Для выхода нажмите любой символ")