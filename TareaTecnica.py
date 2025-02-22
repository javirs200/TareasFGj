from Utils import Input
from Utils import ui

from Cryptography import Cesar

#funcion principal
def main():

    ui.showEmptyLine()

    #obtencion de los parametros de entrada
    index,text,option = Input.getInputs()

    ui.showReadedParams(index,text,option)

    ui.showEmptyLine()
    
    #seleccion de la opcion de cifrado o descifrado
    if option == "-c":
        #cifrado
        output = Cesar.encrypt(text, index)
        ui.showEncryptedText(output)
        
    elif option == "-d":
        #descifrado
        output = Cesar.decrypt(text, index)
        ui.showDecryptedText(output)
        
    pass

if __name__ == '__main__':
    main()