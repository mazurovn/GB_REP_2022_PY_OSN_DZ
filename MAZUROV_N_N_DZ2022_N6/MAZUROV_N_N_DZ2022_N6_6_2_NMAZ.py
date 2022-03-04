
# Домашнее задание 6 задача 6 2 Nikolay Mazurov
# ver 2.0 alfa


"""


"""


########################  ЗАПИСЬ  ########################
from itertools import zip_longest
import sys
import argparse

bake=[]
price = []
x = 1000000
y= 10

print(f"число {x}\n\n")

with open("bakery.csv","r",encoding="utf-8") as add_item:
    with open("bakery.csv","r",encoding="utf-8") as add_item_second:

        if  len(sys.argv) > 1 and [ch for ch in sys.argv[1:] if "." in ch.replace(".","").isdigit()]:

            if round(float(sys.argv[1:]), 3) <= x:

                print(f"{round(float(sys.argv[1]), 3):>{y}}", file=add_item)

            else:

                print(f"Число меньше {x} ")


        else:
                print(add_item_second.read())

file = "bakery.csv"
price_bake = open(file, "r",encoding="utf-8")
print(type(price_bake))
print(price_bake.read())
x = input("\n\nВедите символ для выхода.\n")
