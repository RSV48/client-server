import unittest
import functions


class TestFunctions(unittest.TestCase):
    param = {'-p 0.0.0 1024': None,
             '-p 0.0.0.0 35': None,
             '-p 0.0.0.0': None,
             '-p 0.0.0.0 1245': ('0.0.0.0', 1245),
             'default': ('localhost', 7777)}

    def test_Parser_false_param(self):
        for key, value in self.param.items():
            if key == 'default':
                self.assertEqual(functions.createParser(), value, f'Ошибка в тесте {key.split()}')
            else:
                print(key.split())

                self.assertEqual(functions.createParser(key.split()), value,
                                 f'Ошибка в тесте {key.split()}')


if __name__ == "__main__":
    unittest.main()
