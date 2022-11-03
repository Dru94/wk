from cryptography.fernet import Fernet
import time
import sys


def genKey():
    key = Fernet.generate_key()
    f = Fernet(key)
    
    return f

def encryptText(key, text):
    token = key.encrypt(text.encode())
    return token

def decryptText(key, text):
    token = key.decrypt(text).decode()
    return token

if __name__ == "__main__":
    
    text = input("Enter text to encrypt here: ")
    
    key = genKey()
    encText = encryptText(key, text)
    print("Your encrypted text is", encText)
    
    time.sleep(1)
    print("Decrypting text to back to original.")
    time.sleep(2)
    decText = decryptText(key, encText)
    print("Original text: ", decText)
    sys.exit()

    
