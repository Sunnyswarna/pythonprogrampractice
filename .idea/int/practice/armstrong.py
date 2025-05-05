number = int(input('enter the number:'))
armstrong_sum=0
length = len(str(number))

while number > 0 :
    digit = number % 10
    armstrong_sum += digit ** length
    number //= 10
if armstrong_sum == number:
    print('the number is armstrong number',armstrong_sum) 
else:
    print('the number is not armstrong number',armstrong_sum)
    
    
    
