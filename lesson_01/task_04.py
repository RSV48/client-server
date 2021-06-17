"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode)."""

str_list = ['разработка', 'администрирование', 'protocol', 'standard']


def convertingArr(arr, param='encode'):
    for i, value in enumerate(arr):
        if param == 'encode' and not isinstance(value, bytes):
            arr[i] = value.encode('utf-8')
        elif param == 'decode' and isinstance(value, bytes):
            arr[i] = value.decode('utf-8')


print(f'{10*"*"} Строковое предствление списка {10*"*"}')
print(str_list)

print(f'{10*"*"} Преобразованное в байтовое предствление списка {10*"*"}')
convertingArr(str_list)
print(str_list)

print(f'{10*"*"} Преобразованное в строковое предствление списка {10*"*"}')
convertingArr(str_list, 'decode')
print(str_list)

""" РЕЗУЛЬТАТ
********** Строковое предствление списка **********
['разработка', 'администрирование', 'protocol', 'standard']

********** Преобразованное в байтовое предствление списка **********
[b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0', 
b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', 
b'protocol', b'standard']

********** Преобразованное в строковое предствление списка **********
['разработка', 'администрирование', 'protocol', 'standard']

"""