import random
n= random.randint(1,10)
guess=0
while guess!=n:
    guess=int(input('enter a number'))
    if guess<n:
        print('number is smaller')
    elif guess>n:
        print('number is larger')
    else:
        print('yes :')

