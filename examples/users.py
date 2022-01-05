from pyduinocoin import DuinoClient

client = DuinoClient()
username = '' # Input username

try:
    result = client.user(username)
except Exception as error:
    print(error)
else:
    print('Balance: ' + str(result.balance.balance))
    
    print('Miners: ')
    for miner in result.miners:
        print(miner)

    print('Transactions: ')
    for transaction in result.transactions:
        print(transaction)