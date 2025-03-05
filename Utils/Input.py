import sys

from Utils import ui

def getInputs() -> tuple[int,str,str]:
    
    #lectura de argumentos de la linea de comandos
    if len(sys.argv) == 4:
        argIndex = sys.argv[1]
        argText = sys.argv[2]
        argOption = sys.argv[3]
    else:
        # si el numero de argumentos no es el correcto se muestra un mensaje de error
        ui.shownumberofargumentsError()
        # si el numero de argumentos es incorecto se detiene el programa y se muestra las instrucciones de uso
        ui.showUsage()
        sys.exit()

    #validacion de los argumentos de entrada
    _validateInputs(argIndex,argText,argOption)

    #conversion de los argumentos genericos a los tipos de datos correctos
    index = int(argIndex)
    text = str(argText)
    option = str(argOption)
    
    return index,text,option

#funcion para validar los argumentos de entrada segun especificaciones
def _validateInputs(index:str,text:str,option:str):

    error = False

    # comprobacion del indice como numerico
    if not index.isdigit():
        # si el indice no es numerico muestra un mensaje de error
        ui.showindexError()
        error = True

    # comprobacion del texto
    if text.isdigit():
        # si el texto es unicamente numerico muestra un mensaje de error
        ui.showtextError()
        error = True

    # comprobacion de la opcion
    if option != "-c" and option != "-d":
        # si la opcion no es -c o -d muestra un mensaje de error
        ui.showoptionError()
        error = True
    
    if error:

        ui.showUsage()
        sys.exit()
    
    return not error 