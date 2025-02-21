
def encrypt(text:str,index:int)->str:
    encryptedText = ""
    for c in text:
        if c.isalpha() and not c.isspace():

            if c.isupper():
                baseChar = 'A'
            else:
                baseChar = 'a'

            c = chr((ord(c) + index - ord(baseChar)) % 26 + ord(baseChar))

        encryptedText += c

    return encryptedText

def decrypt(text:str,index:int)->str:
    
    decryptedText = encrypt(text,-index)

    return decryptedText