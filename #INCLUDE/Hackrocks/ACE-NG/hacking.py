from Cryptodome.Cipher import AES

key = b"verylonglongkeyy"
iv = b"1234567890987654"

ciphertext = bytes.fromhex(
    "d63f6428c8cad27db03e2a228ca74df83a35a49b37e747a7a434bce27f43d649ecbf68863a"
)

print(ciphertext)

cipher = AES.new(key, AES.MODE_CFB, iv=iv)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode(errors="replace"))

#flag{PyInstaller_AES_malware_example}