# Домашнее задание 4 задача 2 Nikolay Mazurov
# ver 2.0 alfa




# !!!!!!!!!!!!!!! ПОШЛА ЗАЩИТА ОТ DDOS !!!  И  СКРИПТ НЕ ВСЕГДА ПРОХОДИТ !!!
 # Мы зарегистрировали подозрительный трафик исходящий из вашей сети.!!!!!
# С помощью этой страницы мы сможем определить, что запросы отправляете именно вы, а не робот.!!!!!!
# ДУМАЮ КАК ОБОЙТИ



"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и 
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна 
возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами 
использоватьвместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код 
валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был 
передан аргумент? В качестве примера выведите курсы доллара и евро.
"""

import requests

from requests import get, utils
check = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))
#________Функция ____
def currency_rate(parcng):
    value = check.split("<Valute ID=") # режим  и добываем значения
    for i in value:
        if parcng.upper() in i:
            print(parcng.upper(), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))  # берем нужное значение
print(currency_rate("uSd"))  # выводим и приводим к значению USD
print(currency_rate("EUR"))  # выводим
