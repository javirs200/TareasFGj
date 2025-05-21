from binascii import hexlify as heg , unhexlify as unheg
import requests

FLAG = str(int(heg(heg(heg(b"the code secret is 'i_eat_a_lot_of_pancakes' !!!!"))).decode('utf-8')) ^ 15).encode()

print("flag: ", FLAG)

# 1. decode the flag into string
decoded_flag = FLAG.decode()

print("decoded_flag: ", decoded_flag) 

# 2. reverse the XOR operation with 15
decoded_flag = int(decoded_flag) ^ 15

# 3. convert the integer back to bytes
decoded_flag = str(decoded_flag).encode()

# 4. reverse de heg 3 times
decoded_flag = unheg(decoded_flag)
decoded_flag = unheg(decoded_flag)
decoded_flag = unheg(decoded_flag)

# 5. decode the bytes into string
decoded_flag = decoded_flag.decode()

print(decoded_flag) # the code secret is 'i_eat_a_lot_of_pancakes' !!!!