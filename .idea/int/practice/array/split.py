#l1=[1,2,3,4,5,6,7,8,9,10]
l1=int(input['enter the nummbers:'])
l2=[]
l3=[]
for i in l1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
print('even numbers:',l2)  
print('odd numbers:',l3)