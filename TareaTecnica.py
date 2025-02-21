from Utils import Input
from Utils import ui

from Cryptography import Cesar

def main():
    index,text,option = Input.getInputs()
    ui.showReadedParams(index,text,option)
    
    if option == "-c":
        output = Cesar.encrypt(text, index)
        ui.showEncryptedText(output)
        
    elif option == "-d":
        output = Cesar.encrypt(text, index)
        ui.showDecryptedText(output)
        
    pass

if __name__ == '__main__':
    main()