# Домашнее задание 1 задача 1 Nikolay Mazurov
# ver 2.0 alfa

"""
### 1. Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности
duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток:
<h> час <m> мин <s> сек;
 * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:

duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
"""




sec = int(input('введите  duration:  ')) # вводим значение в переменную
day = sec // (3600 * 24) # Дни
hour = sec // 3600 % 24 # часы
min = sec % 3600 // 60  # Минуты
sec = sec % 3600 % 60 # Секнды
# print(sec,'секунд')
# print(min,'минут',sec,'секунд')
# print(hour,'часов',min,'минут',sec,'секунд')
print (day,'дня',hour,'часов',min,'минут',sec,'секунд')
exit_in = input('для выхода нажмите любую букву')
