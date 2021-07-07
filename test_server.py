import json
import unittest
import server


class TestServer(unittest.TestCase):
    param = [{"action": "presence:", "time": " ", "user": "Roman", },
             '',
             {"action": "presence:", "time": " ", "user": "Alex", }
             ]

    def test_msg_200(self):
        msg = json.dumps(self.param[0])
        self.assertEqual(server.createResponseMsg(msg.encode('utf-8')),
                         {"response": 200, "alert": 'Добрый день, Roman!'},
                         f'Ошибка в тесте {msg}')

    def test_msg_400(self):
        msg = json.dumps(self.param[1])
        self.assertEqual(server.createResponseMsg(msg.encode('utf-8')),
                                                  {"response": 400, "alert": 'Не верный формат сообщения'},
                                                  f'Ошибка в тесте')

    def test_msg_402(self):
        msg = json.dumps(self.param[2])
        self.assertEqual(server.createResponseMsg(msg.encode('utf-8')),
                         {"response": 402, "alert": 'Не верный логин'},
                         f'Ошибка в тесте {msg}')


if __name__ == "__main__":
    unittest.main()
