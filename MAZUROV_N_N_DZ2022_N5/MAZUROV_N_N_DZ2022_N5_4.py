
# Домашнее задание 5 задача 4 Nikolay Mazurov
# ver 2.0 alfa


"""
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:

('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.

### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```

"""

src = [2, 2, 9, 7, 23, 1, 60, 44, 3, 2, 10, 7, 4, 11, 22, 2]
list = []
check = []

for ch in src:
    if ch in check:
        continue
    if ch in list:
        check.append(ch)
        list.remove(ch)
        continue
    list.append(ch)
print(src)
print(list)