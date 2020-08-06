text = input('Enter text:')

text2 = text.replace(' ','')

text_lower = text2.lower()
text_rev = text_lower [::-1]
if text_lower == text_rev:
    print('palindorme')
else:
    print('not palindorme')




