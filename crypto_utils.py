from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os
#from dotenv import load_dotenv

#load_dotenv()

#SECRET_KEY = os.getenv('SECRET_KEY').encode()
'''
To do this securely, you should store the SECRET_KEY in an environment variable or a secure vault. Here we will hardcode this for simplicity sake. 

'''

SECRET_KEY = 'abcdefghijklmnop'  # Must be 16, 24, or 32 bytes long


def encrypt_data(plain_text):
    cipher = AES.new(SECRET_KEY.encode(), AES.MODE_CBC)
    iv = cipher.iv
    encrypted = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted).decode('utf-8')


def decrypt_data(encrypted_data):
    data= base64.b64decode(encrypted_data)
    iv = data[:AES.block_size]
    cipher = AES.new(SECRET_KEY.encode(), AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(data[AES.block_size:]), AES.block_size)
    return decrypted.decode('utf-8')


'''

example main for debugging:

if __name__ == "__main__":
    plain_text = "This is a secret message that needs to be encrypted."
    encrypted = encrypt_data(plain_text)
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt_data(encrypted)
    print(f"Decrypted: {decrypted}")  # Should print "my super secret password" if successful


'''
