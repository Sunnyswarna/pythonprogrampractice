sum=0
for i in range(1,101):
    if i % 2 == 0:
        print(i)
        sum+=i
print('Sum of even numbers from 1 to 100 is:',sum)