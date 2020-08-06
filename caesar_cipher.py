# ask the user to enter the open (unencrypted), one-line message
text = input("Enter your message: ")
cipher = ''  # prepare a string for an encrypted message (empty for now)
for char in text:  # start the iteration through the message
    if not char.isalpha():  # if the current character is not alphabetic
        continue  # ignore it
    char = char.upper()  # convert the letter to upper-case (it's preferable to do it blindly, rather than check whether it's needed or not)
    code = ord(char) + 1  # get the code of the letter and increment it by one
    if code > ord('Z'):  # the resulting code has "left" the Latin alphabet (if it's greater than the Z code)
        code = ord('A')  # change it to the A code
    # append the received character to the end of the encrypted message
    cipher += chr(code)

print(cipher)  # print the cipher

# Caesar cipher - decrypting a message
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
