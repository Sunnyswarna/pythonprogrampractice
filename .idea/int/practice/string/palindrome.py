text = input('Enter a string: ')
rev_text= text[::-1]
if text == rev_text:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')