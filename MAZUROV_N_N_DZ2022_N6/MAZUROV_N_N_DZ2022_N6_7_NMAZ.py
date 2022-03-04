
# Домашнее задание 6 задача 1 Nikolay Mazurov
# ver 2.0 alfa


"""


"""





from itertools import zip_longest
import sys
import argparse

bake = []
price = []
x = 2000000
y = 101
print(f"число {x}\n\n")
print(f"число {y}\n\n")

with open("bakery.csv","r+", encoding="utf-8") as count:
    num, price = sys.argv[1:]
    price= round(float(price.replace(".","")), 3)

    for sale in range(int(num)):
        number = count.tell()
        stroka = count.readline().strip()
        if stroka == "":
            exit("Такой строки в документе нет.  \n ! Ошибка ввода!")
    if "," in str(price) or "." in str(price):
        if price <= x:
            count.seek(number)
            count.write(f"{price:>{y}}")

        else:
            print(f"Укажите значени меньше{x}")



file = "bakery.csv"
price_bake = open(file, "r",encoding="utf-8")
print(type(price_bake))
print(price_bake.read())
x = input("\n\nВедите символ для выхода.\n")
