# Программа клиента для отправки приветствия серверу и получения ответа
import json
from socket import *
from functions import createParser


def createPresenceMsg():
    return {
        "action": "presence:",
        "time": " ",
        "user": "Roman",
    }


def exchange_msg():
    server = createParser()
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(server)  # Соединиться с сервером
    msg = json.dumps(createPresenceMsg())
    s.send(msg.encode('utf-8'))
    data = s.recv(1000000)
    msg = json.loads(data.decode('utf-8'))
    if msg.get('response') == 200:
        return f'Связь установлена: {msg.get("alert")}'
    return f'Что то пошло не так: {msg.get("alert")}'
    s.close()


if __name__ == '__main__':
    result = exchange_msg()
    print(result)
