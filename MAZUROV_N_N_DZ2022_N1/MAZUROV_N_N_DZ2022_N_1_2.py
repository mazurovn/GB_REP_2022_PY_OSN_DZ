# Задание 1 пункт 2
# Nmaz
sum_cubes = 0
value = 0
cubes = []
cube_to = []

# Cоздать список, состоящий из кубов нечётных чисел от 1 до 1000.
for i in range(1, 1000, 2):  #
    cubes.append(i ** 3)  # возведение в куб.

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

for index, i, in enumerate(cubes):
    value = 0

    while i > 0:
        value += i % 10
        i //= 10

    if value % 7 == 0:
        sum_cubes += cubes[index]
print((sum_cubes),': сумма цифр которых делится нацело на 7.')


# К каждому элементу списка добавить 17  и заново вычислить сумму тех чисел из
# этого списка, сумма цифр которых делится нацело на 7.


for value_plus in cubes:
    cube_to.append(value_plus + 17)

# Повторное вычесление с новыми значениями + 17.
sum_cubes = 0
for index, i in enumerate(cube_to):  #
    value = 0

    while i > 0:
        value += i % 10
        i //= 10

    if value % 7 == 0:
        sum_cubes += cube_to[index]
print((sum_cubes),': сумма цифр которых делится нацело на 7 и к которым добавили 17.')
x = input("Для выхода нажмите любой символ")
