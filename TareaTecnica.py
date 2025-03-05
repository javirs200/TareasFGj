from Utils import Input
from Utils import ui

from Cryptography import Cesar

#funcion principal
def main():

    ui.showEmptyLine()

    #obtencion de los parametros de entrada y su validacion
    index,text,option = Input.getInputs()

    ui.showReadedParams(index,text,option)

    ui.showEmptyLine()
    
    #seleccion de la opcion de cifrado o descifrado ( las opciones ya entran validadas aqui las valida getInputs, no es necesario validarlas de nuevo)
    if option == "-c":
        #cifrado
        output = Cesar.encrypt(text, index)
        ui.showEncryptedText(output)
        
    elif option == "-d":
        #descifrado
        output = Cesar.decrypt(text, index)
        ui.showDecryptedText(output)
        

if __name__ == '__main__':
    main()