
# Домашнее задание 5 задача 3 Nikolay Mazurov
# ver 2.0 alfa


"""

 Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...


"""



from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

class_tutor = ((tutor, klass) for tutor, klass in zip_longest(tutors, classes) if tutor)
print(type(class_tutor))
for ch in class_tutor:
    print(ch)


x= input("Ведите символ для выхода.\n")
