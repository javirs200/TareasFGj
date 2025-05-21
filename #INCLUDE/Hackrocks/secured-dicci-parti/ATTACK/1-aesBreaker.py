#PyCryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# aprovechando la debilidad de randint 
def generar_clave(semilla):
    return (str(semilla).zfill(5) * 4)[:16].encode()

# funcion para validadr las claves
def encrypt(plaintext, a, b):
    cipher = AES.new(a, mode=AES.MODE_ECB)
    ct = cipher.encrypt(pad(plaintext, 16))
    cipher = AES.new(b, mode=AES.MODE_ECB)
    ct = cipher.encrypt(ct)
    return ct.hex()


plaintext = b"AAAAAAAAAAAAAAAA"   
ciphertext = bytes.fromhex("16b1fadc7a5986443843281d8875d0f51a2e2573e34946df1ad0c23887d949b0") 

posibles_clave1_padded_cipher = {}
for i in range(100000):
    clave1 = generar_clave(i)
    cipher1 = AES.new(clave1, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, 16)
    intermediate_cipher = cipher1.encrypt(padded_plaintext)
    posibles_clave1_padded_cipher[intermediate_cipher] = clave1

for j in range(100000):
    clave2 = generar_clave(j)
    cipher2_inv = AES.new(clave2, AES.MODE_ECB)
    try:
        intermediate_with_padding = cipher2_inv.decrypt(ciphertext)

        if intermediate_with_padding in posibles_clave1_padded_cipher:
            clave_encontrada_1 = posibles_clave1_padded_cipher[intermediate_with_padding]
            clave_encontrada_2 = clave2
            print(f"¡Clave 1 encontrada: {clave_encontrada_1}")
            print(f"¡Clave 2 encontrada: {clave_encontrada_2}")

            # validacion de las claves
            double_encrypted = encrypt(plaintext, clave_encontrada_1, clave_encontrada_2)
            if double_encrypted == ciphertext.hex():
                print(f"¡Las claves son correctas! {clave_encontrada_1} y {clave_encontrada_2}")
            break
    except ValueError as e:
        # Manejar posibles errores de descifrado
        pass