import os
import pyaes

file_name = 'CryptAll.txt.ransomware'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

key = b'1234567890123456'  # 16 bytes key for AES-128
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)
os.remove(file_name)  # Remove the encrypted file

new_file = 'rb'
new_file  = open(f'{new_file}', 'rb')
new_file.write(decrypted_data)
new_file.close()