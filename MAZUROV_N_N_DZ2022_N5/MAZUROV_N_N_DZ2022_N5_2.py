
# Домашнее задание 5 задача 2 Nikolay Mazurov
# ver 2.0 alfa


"""

1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...

2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.



"""



i= int(input("Ведите число до которого генерировать нечетные числа : \n      "))
gen_nechet = (nums for nums in range(1, i + 1, 2))

for nums in gen_nechet:
    print(nums)
x= input("Ведите символ для выхода.\n")

