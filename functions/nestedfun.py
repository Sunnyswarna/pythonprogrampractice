def closure():
    msg='HELLO'
    def display():
        print('x'*10)
        print(msg)
        print('x'*10)
    return display
d=closure()
d()