import yaml

data = {
    '1': [],
    '2': 25,
    '3': {
        '1₽': '1',
        '2ʥ': '2',
        '3ʨ': '3'
    }
}

with open('yaml_file.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open('yaml_file.yaml') as file:
    print(file.read())
