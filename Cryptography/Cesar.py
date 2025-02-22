
def encrypt(text:str,index:int)->str:
    #variable para almacenar el texto resultante
    encryptedText = ""
    # bucle para realizar el cifrado de cada caracter del texto
    for c in text:
        #comprobacion de caracteres y espacios para evitar signos de puntuacion , numeros y los espacios 
        if c.isalpha() and not c.isspace():

            #asignacion de caracter base en funcion de mayusculas y minusculas
            if c.isupper():
                baseChar = 'A'
            else:
                baseChar = 'a'

            #formula general explicada en el PDF
            c = chr((ord(c) + index - ord(baseChar)) % 26 + ord(baseChar))

        #concatenacion en el texto resultante
        encryptedText += c

    return encryptedText

def decrypt(text:str,index:int)->str:
    
    #se realiza el desplazamiento con el indice negativo para obtener el texto en claro
    decryptedText = encrypt(text,-index)

    return decryptedText