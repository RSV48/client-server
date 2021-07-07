# Программа сервера для получения приветствия от клиента и отправки ответа
import json
from socket import *
from functions import createParser, send_msg


def createResponseMsg(msg):
    try:
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
    except AttributeError:
        return {
            "response": 400,
            "alert": "Не верный формат сообщения"
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
        send_msg(client, createResponseMsg(data))
        client.close()


if __name__ == '__main__':
    responseMsg()
