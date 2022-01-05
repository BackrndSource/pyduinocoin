from unittest import TestCase
from pyduinocoin import DuinoClient, PyDuinoCoinException


class PyDuinoCoinExceptionTests(TestCase):
    def setUp(self):
        self.client = DuinoClient()

    def test_exception_user_not_found(self):
        try:
            self.client.user('sdgsdgerhdfhbxsge4tery56rsgsgr')
        except PyDuinoCoinException as exception:
            self.assertTrue(isinstance(exception, PyDuinoCoinException))
            self.assertIn('sdgsdgerhdfhbxsge4tery56rsgsgr not found', exception.args[0])
         
