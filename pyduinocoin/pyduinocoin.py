import requests
from .exceptions import PyDuinoCoinException
from .dict_obj import DictObj


class DuinoClient():
    '''
    API REST documentation:
    https://github.com/revoxhere/duco-rest-api
    '''

    def __init__(self):
        self._base_url = 'https://server.duinocoin.com/'

    def _get(self, endpoint, params='', results_key='result'):
        '''
        '''
        url = '{}{}'.format(self._base_url, endpoint)
        response = requests.request("GET", url, params=params)

        if response.status_code == 200:
            json = response.json()

            if ('success' in json and json['success'] == False) or 'message' in json:
                raise PyDuinoCoinException(json['message'] if 'message' in json else 'Unknown error')

            if results_key:
                if isinstance(json[results_key], list):
                    return [DictObj(item) if isinstance(item, dict) else item for item in json[results_key]]
                else:
                    return DictObj(json[results_key])

            return DictObj(json)
        else:
            raise PyDuinoCoinException('SERVER REQUEST ERROR (' + str(response.status_code) + ')')


    def user(self, username, limit=5):
        '''
        Return username's balance, last transactions and miners in one request.
        '''

        return self._get(f'users/{str(username)}', {'limit':limit})

    def auth(self, username, password):
        '''
        Check username's password.
        '''
        
        return self._get(f'auth/{str(username)}', {'password':password})

    def transactions(self, hash=None, limit=None):
        '''
        Return all transactions or an unique transaction with that hash.
        '''
        
        return self._get(f'transactions/{str(hash)}') if hash else self._get('transactions', {'limit':limit} if limit else {}) 

    def user_transactions(self, username, limit=10):
        '''
        Return transactions related to username.
        '''

        return self._get(f'user_transactions/{str(username)}', {'limit':limit})

    def id_transactions(self, id):
        '''
        Return a transaction with that id.
        '''

        return self._get(f'id_transactions/{str(id)}')

    def transfer(self, username, password, recipient, amount, memo='Powered by pyduinocoin'):
        '''
        Transfer funds from username to recipient.
        '''

        return self._get('transaction', {'username':username, 'password':password, 'recipient':recipient, 'amount':amount, 'memo':memo}, results_key=None)

    def miners(self, username=None, limit=None):
        '''
        Return all miners or username's miners.
        '''

        return self._get(f'miners/{str(username)}', {'limit':limit} if limit else {}) if username else self._get('miners', {'limit':limit} if limit else {})
    
    def balances(self, username=None, limit=None):
        '''
        Return all balances or username's balance.
        '''

        return self._get(f'balances/{str(username)}') if username else self._get('balances', {'limit':limit} if limit else {})

    def statistics(self):
        '''
        Return server statistics.
        '''

        return self._get('statistics', results_key=None)

    def all_pools(self):
        '''
        Return all non-hidden mining pools.
        '''

        return self._get('all_pools')

    def exchange_request(self, username, password, email, type, amount, coin, address):
        '''
        Submit exchange request in the DUCO Exchange.
        '''

        return self._get('exchange_request', {'username':username, 'password':password, 'email':email, 'type':type, 'amount':amount, 'coin':coin, 'address':address}, results_key=None)