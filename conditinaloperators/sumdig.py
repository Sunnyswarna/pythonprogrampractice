number= int(input('enter the number'))
sum = 0
while number>0:
    r= number % 10
    number= number//10
    sum= sum + r
print("sum of dig=",sum)