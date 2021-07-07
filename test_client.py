import unittest
import client


class TestClient(unittest.TestCase):

    def test_createPresenceMsg(self):
        self.assertEqual(client.createPresenceMsg(), {"action": "presence:", "time": " ", "user": "Roman", })


if __name__ == "__main__":
    unittest.main()
