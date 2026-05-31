from time import time
from security.manageTokens import unencryptTokens, refreshTokens

def retrieveLoc(person: str):
    accessToken, refreshToken, expiresAt = unencryptTokens(person)

    # --- Step 3 ---
    if time() >= expiresAt - 300: # If token will expire in 300s or less
        print("**retrieveLoc.py** - Access token expired; refreshing")
        accessToken = refreshTokens(person)

if __name__ == "__main__":
    retrieveLoc("mom")