# module for Caesar criptography algorithm
# Authors: Javier Miranda
# version: 1.2.0

# libreria para expresiones regulares	
import re

def encrypt(text:str,index:int)->str:
    #variable para almacenar el texto resultante
    encryptedText = ""
    # bucle para realizar el cifrado de cada caracter del texto
    for c in text:
        #comprobacion de caracteres mediante expresion regular 
        # para evitar signos de puntuacion , numeros , espacios y carcteres especiales 
        if re.match('[a-zA-Z]',c):

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
    
    #se realiza el cifrado con el indice de desplazamiento negativo para obtener el texto en claro
    decryptedText = encrypt(text,-index)

    return decryptedText