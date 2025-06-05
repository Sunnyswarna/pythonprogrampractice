vowels='a''e''i''o''u'
vowels_count=0
sentence=input("Enter a sentence: ")
for i in sentence:
    if i in vowels:
        vowels_count+=1
print("Number of vowels in the given sentence is:",vowels_count)