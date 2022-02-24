# Домашнее задание 3 задача 3 Nikolay Mazurov
# ver 2.0 alfa
"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
начинающиеся с соответствующей буквы. Например:

>>>  thesaurus("Иван", "Мария", "Мария", "Илья")
 {
     "И": ["Иван", "Илья"],
     "М": ["Мария"], "П": ["Петр"]
 }

 Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если
 потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
"""



def thesaurus(*find_name):
    list_name = {} # словарь с именами
    for name in find_name:# находим имена
        key = name[0].capitalize() # берем  заглавную букву первую
        if key not in list_name:
            list_name[key] = []
        list_name[key].append(name) #добовляем в список  с именами
    return list_name

print(thesaurus("Иван", "Мария", "Мария", "Илья"))


x = input("Для выхода нажмите любой символ \n")