# Домашнее задание 2 задача 5 Nikolay Mazurov
# ver 1.0

"""""
# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна
# отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
# как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих
# товаров по возрастанию, написав минимум кода?
"""


shop= [57.8, 46.51, 97, 45, 77, 55, 33, 12, 38.44, 64, 13.65, 90, 101.3,]
for check in shop:
    rub, kop = f'{check:.2f}'.split(".") # форматируем и добовляем нули и создаем список разделяя значения.
    print(f"{rub} руб {kop} коп,", end= "  ",)

print(" \n ")
print(" \n ___________sort___по возрастанию____ \n")
print(f"ВЫВОД СПИСКА: - {shop} \n ВЫВОД ID для проверки: {id(shop)} \n")

shop.sort()
print(f"ВЫВОД СПИСКА: {shop} \n   ВЫВОД ID для проверки: {id(shop)} \n")


print("\n ___________sort__5 самых дорогих товаров из списка_____ \n")
new_shop = sorted(shop , reverse=True)
print(f" 5 самых дорогих товаров: \n {new_shop[:5][::-1]} \n ВЕСЬ СПИСОК :  {new_shop}\n ВЫВОД ID для проверки:   {id(new_shop)} \n")

x = input("Для выхода нажмите любой символ    \n   ")


