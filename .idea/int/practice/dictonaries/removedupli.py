d1= {'a': 1, 'b': 2, 'c': 3,'b':2}
D2= {}
for key, value in d1.items():
    if value not in D2.values():
        D2[key]=value
print('Dictionary:',D2)