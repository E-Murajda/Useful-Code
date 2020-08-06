text = 'abracadabra'  # input('Enter 1st text :')
text2 = 'carimari'  # input('Enter 2nd text :')
text_lower = text.lower()
text_lower_r = text.replace(' ', '')
text2_lower = text2.lower()
text2_lower_r = text2.replace(' ', '')
text_lower_l = sorted(text_lower_r)
text2_lower_l = sorted(text2_lower_r)
if text_lower_l == text2_lower_l:
    print('Anagram')
else:
    print('not anagram')
