import csv
import os
import re

catalog = 'data'


def get_data(name_catalog):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for name_file in os.listdir(name_catalog):
        with open(os.path.join(catalog, name_file), 'r', encoding='cp1251') as file:
            for line in file:
                if re.search('Изготовитель системы', line):
                    os_prod_list.append(line[line.find(':') + 1:].strip())
                elif re.search('Название ОС', line):
                    os_name_list.append(line[line.find(':') + 1:].strip())
                elif re.search('Код продукта', line):
                    os_code_list.append(line[line.find(':') + 1:].strip())
                elif re.search('Тип системы', line):
                    os_type_list.append(line[line.find(':') + 1:].strip())

    for i in range(len(os.listdir(catalog))):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    return main_data


def write_to_csv():
    with open('report.csv', 'w') as file:
        report_file = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in get_data(catalog):
            report_file.writerow(row)


write_to_csv()

with open('report.csv') as file:
    print(file.read())

