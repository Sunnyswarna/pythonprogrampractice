n=int(input('enetr a number'))
count=0
while n>0:
    n=n//10
    count += 1
print('number of digits',count)
