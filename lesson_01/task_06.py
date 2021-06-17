"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое."""

import locale

line_list = ['сетевое программирование', 'сокет', 'декоратор']

encode_default = locale.getpreferredencoding()

# Создаем файл test_file.txt со строками line_list с кодировкой по умолчанию utf-8
with open('test_file.txt', 'w') as file:
    for line in line_list:
        file.write(f'{line} \n')
    print(f'Кодировка файла по умолчанию: {file}')


try:
    with open('test_file.txt', 'r', encoding=encode_default) as file:
        for line in file:
            print(line)
except UnicodeDecodeError as err:
    print('Не верная кодировка')
