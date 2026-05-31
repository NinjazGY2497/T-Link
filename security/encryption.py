from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

loadedKey = os.getenv("TOKEN_ENCRYPTION_KEY").encode()
encryptionRecipe = Fernet(loadedKey)

def encrypt(data):
    return encryptionRecipe.encrypt(data.encode()).decode()

def decrypt(token):
    return encryptionRecipe.decrypt(token).decode()

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    print(encrypt(text))