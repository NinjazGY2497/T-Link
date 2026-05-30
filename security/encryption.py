from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

loadedKey = os.getenv("TOKEN_ENCRYPTION_KEY").encode()
encryptionRecipe = Fernet(loadedKey)

def encrypt(data):
    return encryptionRecipe.encrypt(data.encode())

def decrypt(token):
    return encryptionRecipe.decrypt(token).decode()

if __name__ == "__main__":
    print(encrypt("Hello World"))