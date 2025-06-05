D1= 'its a sunny day oustsie'
freq = {}
for i in D1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print('Frequency:',freq)