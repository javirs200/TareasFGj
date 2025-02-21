import sys

from Utils import ui

def getInputs()->int|str|str:
    
    if len(sys.argv) == 4:
        argIndex = sys.argv[1]
        argText = sys.argv[2]
        argOption = sys.argv[3]
    else:
        ui.showUsage()
        sys.exit()

    _validateInputs(argIndex,argText,argOption)

    index = int(argIndex)
    text = str(argText)
    option = str(argOption)
    
    return index,text,option

def _validateInputs(index,text,option):

    error = False

    if not index.isdigit():
        ui.showindexError()
        error = True

    if text.isdigit():
        ui.showtextError()
        error = True

    if option != "-c" and option != "-d":
        ui.showoptionError()
        error = True
    
    if error:
        ui.showUsage()
        sys.exit()
    
    return not error 