from time import time
from security.manageTokens import loadTokens, refreshTokens

def retrieveLoc(person: str):
    accessToken, refreshToken, expiresAt = loadTokens(person)

    # --- Step 3 ---
    if time() >= expiresAt - 300: # If token will expire in 300s or less
        print("**retrieveLoc.py** - Access token expired, refreshing...")
        accessToken, refreshToken, error = refreshTokens(person, refreshToken)

        if error:
            print(f"**retrieveLoc.py** - ERROR: Failed to refresh tokens: {error}")
            return {"error": str(error)}

        print(f"**retrieveLoc.py** - Refreshed, encrypted, and stored tokens.")

    return { # Mock
        "latitude": None,
        "longitude": None,
        "heading": None,
        "timestamp": None,
        "driving_state": None, # (shift_state)
        "online_state": None,
        "error": None
    }

if __name__ == "__main__":
    retrieveLoc("mom")