import sys # libreria de acceso al sistema operativo

from Utils import ui

def getInputs():
    # inicializamos los parametros con valores por defecto
    index = 13
    text = "Yn threen qr Phon: ybf zbgvibf dhr yyrineba n ryyn l, fboer gbqb, inybene l rkcyvpne ry vzcnpgb qr yn cebcntnaqn ra RRHH."
    option = "-d"

    print(sys.argv)

    #utilizamos la libreria sys para recoger los parametros introducidos por linea de comandos
    if len(sys.argv) == 3:
        index = sys.argv[1]
        text = sys.argv[2]
        option = sys.argv[3]
    else:
        ui.showUsage()
        sys.exit()

    _validateInputs(index,text,option)
    
    return index,text,option

def _validateInputs(index,text,option):

    error = False

    if not index.isdigit():
        ui.showindexError()
        error = True

    if text.isalnum():
        print(text)
        ui.showtextError()
        error = True

    if option != "-c" and option != "-d":
        ui.showoptionError()
        error = True
    
    if error:
        ui.showUsage()
        sys.exit()

    






           