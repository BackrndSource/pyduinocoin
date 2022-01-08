from unittest import TestCase
from pyduinocoin import DuinoClient, DictObj


class DuinoClientTests(TestCase):
    def setUp(self):
        self.client = DuinoClient()

    def test_get_user(self):
        try:
            result = self.client.user('Backrndsource')
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
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

            print(result)
    
    def test_get_user_transactions(self):
        try:
            user_transactions = self.client.user_transactions('Backrndsource', limit=10)
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(user_transactions, list))

            for transaction in user_transactions:  
                self.assertTrue(isinstance(transaction, DictObj))

            print(user_transactions)

    def test_get_miners(self):
        try:
            miners = self.client.miners(limit=10)
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(miners, DictObj))
            print(miners)

    def test_get_user_miners(self):
        try:
            miners = self.client.miners('Backrndsource')
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(miners, list))
            print(miners)

    def test_get_balances(self):
        try:
            balances = self.client.balances()
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(balances, DictObj))
            print(balances)

    def test_get_user_balances(self):
        try:
            balances = self.client.balances('Backrndsource')
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(balances, DictObj))
            print(balances)

    def test_get_statistics(self):
        try:
            statistics = self.client.statistics()
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(statistics, DictObj))
            print(statistics)

    def test_get_all_pools(self):
        try:
            all_pools = self.client.all_pools()
        except Exception as exception:
            self.assertIn('SERVER REQUEST ERROR', exception.args[0])
            print(exception)
        else:
            self.assertTrue(isinstance(all_pools, list))
            print(all_pools)
            