numbers = [2,4,5,3,4,5,6,78,536,5896,90,567,89,45]
div = ''
for i in numbers:
    if i % 3 ==0 and i % 9 ==0: 
        div = i
print('divisible by 3 and 9:', div)