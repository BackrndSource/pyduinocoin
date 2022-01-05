from unittest import TestCase
from pyduinocoin import DuinoClient, DictObj

class DuinoClientTests(TestCase):
    def setUp(self):
        self.client = DuinoClient()

    def test_get_user(self):
        result = self.client.user('Backrndsource')
        self.assertTrue(isinstance(result, DictObj))
        
        self.assertTrue(hasattr(result, 'balance'))
        self.assertTrue(isinstance(result.balance, DictObj))
        self.assertTrue(hasattr(result.balance, 'balance'))
        self.assertTrue(hasattr(result.balance, 'username'))
        self.assertEqual(result.balance.username, 'Backrndsource')
        
        self.assertTrue(hasattr(result, 'miners'))
        self.assertTrue(isinstance(result.miners, list))

        self.assertTrue(hasattr(result, 'transactions'))
        self.assertTrue(isinstance(result.transactions, list))
