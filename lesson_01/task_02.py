"""Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
в последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных."""


def info(arr):
    for item in arr:
        print('Строка: ', item, 'Длинна: ', len(item), 'Тип: ', type(item))


str_list_2 = [b'class', b'function', b'method']

info(str_list_2)

""" РЕЗУЛЬТАТ
        Строка:  b'class' Длинна:  5 Тип:  <class 'bytes'>
        Строка:  b'function' Длинна:  8 Тип:  <class 'bytes'>
        Строка:  b'method' Длинна:  6 Тип:  <class 'bytes'>
"""
