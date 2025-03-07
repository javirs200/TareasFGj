# Main Module of Tarea Tecnica for Goodjob #cero7
# Authors: Javier Miranda
# version: 1.2.0

# importacion de modulos propios
from Utils import Input
from Utils import ui
from Cryptography import Cesar

#funcion principal
def main():

    # linea en blanco para separar la salida de la ejecucion del programa
    ui.showEmptyLine()

    #obtencion de los parametros de entrada y su validacion
    index,text,option = Input.getInputs()
    
    #muestra de los parametros de entrada leidos como feedback
    ui.showReadedParams(index,text,option)

    # linea en blanco para separar la salida de la ejecucion del programa
    ui.showEmptyLine()
    
    #seleccion de la opcion de cifrado o descifrado ( las opciones ya entran validadas aqui, las valida getInputs, no es necesario validarlas de nuevo)
    if option == "-c":
        #cifrado
        output = Cesar.encrypt(text, index)
        # muestra la salida final
        ui.showEncryptedText(output)
        
    elif option == "-d":
        #descifrado
        output = Cesar.decrypt(text, index)
        # muestra la salida final
        ui.showDecryptedText(output)
        

if __name__ == '__main__':
    main()