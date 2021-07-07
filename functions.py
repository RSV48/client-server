import sys
import argparse
import json


def createParser(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--param', nargs='+', default=['localhost', 7777])
    if args:
        namespace = parser.parse_args(args[0])
    else:
        namespace = parser.parse_args(sys.argv[1:])
    try:
        param = (namespace.param[0], int(namespace.param[1]))
        if not 1023 < param[1] <= 65535:
            raise ValueError

        if len(param[0].split('.')) != 4 and param[0] != 'localhost':
            raise ValueError

        if param[0].split('.') == 4 and param[0] != 'localhost':
            ip_adr = ''
            for i, n in enumerate(param[0].split('.')):
                ip_adr += str(int(n)) + '.' if i != 4 else str(int(n))
            param[0] = ip_adr
        print(param)
        return param
    except ValueError:
        print(f'Введено не верное значение параметров')
    except IndexError:
        print('Введите порт!')


def send_msg(socket, msg):
    message = json.dumps(msg)
    socket.send(message.encode('utf-8'))
