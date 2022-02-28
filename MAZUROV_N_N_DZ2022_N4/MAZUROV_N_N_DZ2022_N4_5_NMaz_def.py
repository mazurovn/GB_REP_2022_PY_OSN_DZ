# Домашнее задание 4 задача 5 Nikolay Mazurov
# ver 2.0 alfa




# !!!!!!!!!!!!!!! ПОШЛА ЗАЩИТА ОТ DDOS !!!  И  СКРИПТ НЕ ВСЕГДА ПРОХОДИТ !!!
 # Мы зарегистрировали подозрительный трафик исходящий из вашей сети.!!!!!
# С помощью этой страницы мы сможем определить, что запросы отправляете именно вы, а не робот.!!!!!!
# ДУМАЮ КАК ОБОЙТИ


"""
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:

> python task_4_5.py USD
75.18, 2020-09-05

"""

from requests import get, utils

from datetime import date

check = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rate(parcng):
    value = check.split("<Valute ID=")  # режим  и добываем значения
    d, m, y, = map(int, value[0].split('"')[-4].split("."))  # добываем даты
    for i in value:
        if parcng.upper() in i:
            print(date(year=y, month=m, day=d), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))  # берем нужное значение



# print(currency_rate("uSd"))#выводим и приводим к значению USD
# print(currency_rate("EUR"))#выводим
