# Домашнее задание 4 задача 4 Nikolay Mazurov
# ver 2.0 alfa




# !!!!!!!!!!!!!!! ПОШЛА ЗАЩИТА ОТ DDOS !!!  И  СКРИПТ НЕ ВСЕГДА ПРОХОДИТ !!!
 # Мы зарегистрировали подозрительный трафик исходящий из вашей сети.!!!!!
# С помощью этой страницы мы сможем определить, что запросы отправляете именно вы, а не робот.!!!!!!
# ДУМАЮ КАК ОБОЙТИ


"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться,
что ничего лишнего не происходит.
"""

# Импорт модулей
from requests import get, utils
from datetime import date


check = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rate(parcng):
    value = check.split("<Valute ID=") # режим  и добываем значения
    d, m, y, = map(int, value[0].split('"')[-4].split("."))# добываем даты
    for i in value:
        if parcng.upper() in i:
            print(date(year=y, month=m, day=d), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))#берем нужное значение


# print(currency_rate("uSd"))#выводим и приводим к значению USD
# print(currency_rate("EUR"))#выводим
