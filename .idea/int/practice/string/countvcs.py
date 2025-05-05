str1='this is sunil kumar swarna'
vowels='aeiou'
numbers='0123456789'
space=' '
space_count=0
constants_count=0
vowel_count=0
number_count=0 
for i in str1:
    if i in vowels:
        vowel_count+=1
    elif i in numbers:
        number_count+=1
    
    elif i in space:
        space_count+=1 
    else: 
        constants_count+=1     
print('the number of vowels in the string is:',vowel_count)
print('the number of numbers in the string is:',number_count)
print('the number of constants in the string is:',constants_count)
print('the number of spaces in the string is:',space_count)

        
