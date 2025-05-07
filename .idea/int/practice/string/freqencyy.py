from collections import Counter 
str1 = 'hello world hello'
word_list = str1.split()
str1_frequency = Counter(word_list)
print(str1_frequency)