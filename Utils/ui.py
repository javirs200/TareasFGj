def showUsage():
    print("Uso: python TareaTecnica.py <indice> <texto> <opcion>")
    print("Donde:")
    print("<indice> : un numero entero")
    print("<texto> : una cadena de caracteres")
    print("<opcion> : -c para cifrar el texto, -d para descifrar el texto")

def showindexError():
    print("Error: El parametro indice debe ser un entero")

def showtextError():
    print("Error: El texto debe ser una cadena de caracteres")

def showoptionError():
    print("Error: La opcion debe ser -c o -d")

def showReadedParams(index,text,option):
    print("El indice es: ", index)
    print("El texto es: ", text)
    print("La opcion es: ", option)

def showEncryptedText(output):
    print("Cifrando... \n")
    print("El texto cifrado es: ",output)

def showDecryptedText(output):
    print("Descifrando... \n")
    print("El texto descifrado es: ",output)
    