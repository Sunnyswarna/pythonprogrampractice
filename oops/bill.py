from collections import Counter

prices = {'soap':50, 'toothpaste':25, 'shampoo':45, 'brush':16}

print('items             cost qty   total')
def generate_bill(cart):
    for item, qty in cart.items():
        print(f'{item:10} {prices[item]:10} {qty:2} = {prices[item]*qty}')

cart = Counter(soap =5, toothpaste =1, shampoo  =2, brush =3)
generate_bill(cart)
