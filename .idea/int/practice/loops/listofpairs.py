L1=[3,5,7,5,8,2,4,8,6,5,9,4,2,1]
val=5
pair= 0
for i in range(len(L1)):
    for j in range (i+1,len(L1)):
        if L1[i]+L1[j] == val:
            pair+=1
            print('pair:',L1[i],L1[j])
           
print('pairs:',pair)
            