n= 100
prime_sum = 0

for num in range(2, 101):  # Start from 2, since 1 is not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i  == 0:
            break
        else:
            
            prime_sum += num
            
  

print("Sum of prime numbers up to 100 is:", prime_sum)
 