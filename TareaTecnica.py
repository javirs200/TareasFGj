from Utils import Input
from Utils import ui

from Cryptography import Cesar

def main():

    ui.showEmptyLine()

    index,text,option = Input.getInputs()
    ui.showReadedParams(index,text,option)

    ui.showEmptyLine()
    
    if option == "-c":
        output = Cesar.encrypt(text, index)
        ui.showEncryptedText(output)
        
    elif option == "-d":
        output = Cesar.decrypt(text, index)
        ui.showDecryptedText(output)
        
    pass

if __name__ == '__main__':
    main()