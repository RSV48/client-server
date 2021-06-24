# Программа сервера для получения приветствия от клиента и отправки ответа
import json
from socket import *
from functions import createParser


def createResponseMsg(msg):
    data = json.loads(msg.decode('utf-8'))
    user = 'Roman'
    if data.get('user') == user:
        response = 200
        alert = f'Добрый день, {user}!'
    else:
        response = 402
        alert = 'Не верный логин'
    return {
        "response": response,
        "alert": alert
    }


def responseMsg():
    server = createParser()
    print(server)
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(server)
    s.listen(5)
    while True:
        client, addr = s.accept()
        data = client.recv(1000000)
        print(data)
        print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
        msg = json.dumps(createResponseMsg(data))
        client.send(msg.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    responseMsg()
