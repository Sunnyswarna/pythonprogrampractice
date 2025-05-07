text = 'this is sunny'
replace_text=''
for i in text:
    if i == ' ':
        replace_text = replace_text + '%20'
    else:
        replace_text = replace_text + i
print(replace_text)