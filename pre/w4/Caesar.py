textinput = input("Text : ")
key = int(input("Enter Key"))
text = textinput.lower()
letter = ""
Encrypted_text = ''.join(chr(ord(letter)+3) for letter in text)
print(Encrypted_text)