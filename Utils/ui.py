#modulo que contiene las funciones de impresion en consola

def showUsage():
    print("Uso: Python TareaTecnica.py <indice> <texto> <opcion>\n")
    print("Donde: \n")
    print("<indice> : un numero entero , desplazamiento de caracteres.")
    print("<texto> : una cadena de caracteres , texto a cifrar o descifrar.")
    print("<opcion> : -c para cifrar el texto, -d para descifrar el texto.\n")

def showindexError():
    print("Error, El parametro indice introducido no es un numero entero . \n")

def showindexLowValueError():
    print("Error, El parametro indice debe ser mayor que 0 . \n")

def showtextError():
    print("Error, el texto se ha reconocido como unicamente numerico , debe ser una cadena de texto .\n")

def showoptionError():
    print("Error, la opcion introducida es incorrecta , debe ser -c o -d . \n")

def showNumberofargumentsError():
    print("Error, el numero de argumentos introducidos no es el adecuado , por favor revise las instrucciones de uso . \n")

def showReadedParams(index,text,option):
    print("El indice es: ", index)
    print("El texto es: ", text)
    print("La opcion es: ", option)

def showEncryptedText(output):
    print("Cifrando... \n")
    print("El texto cifrado es: ",output ,"\n")

def showDecryptedText(output):
    print("Descifrando... \n")
    print("El texto descifrado es: ",output ,"\n")

def showEmptyLine():
    print("")   