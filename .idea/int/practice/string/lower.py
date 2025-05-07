text = 'sunny'
converted_text = ''
for i in text:
    converted_text += chr(((ord(i))-32))
print(converted_text)

    