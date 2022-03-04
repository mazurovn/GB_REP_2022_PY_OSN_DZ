
# Домашнее задание 6 задача 2 Nikolay Mazurov
# ver 2.0 alfa


"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей
 вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""



from collections import Counter

st = "!"*40

with open("nginx_logs.txt","r", encoding='utf-8') as find:
    list_of_spammer = Counter()

    for spamm in find:

        list_of_spammer[spamm.split()[0]] += 1

    ip, count = list_of_spammer.most_common(1)[0][0], list_of_spammer.most_common(1)[0][1]

    print(f' {st}\n   !!!  НАЙДЕН  SPAMMER  !!!\n  ЕГО IP - '
          f' {ip} \n КОЛЛИЧЕСТВО СПАММА -   {count} !!! \n {st}')

x= input("Ведите символ для выхода.\n")