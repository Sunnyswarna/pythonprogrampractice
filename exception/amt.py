class AccountBalanceException(Exception):
    pass
balance = 10000
def withdraw(amt):
    global balance
    if balance - amt < 5000:
        raise AccountBalanceException('min amount should be 5000')
    else:
        balance = balance - amt
        print('reaming amount is ',balance)
try:
    withdraw(3000)
except AccountBalanceException as e:
    print(e)
