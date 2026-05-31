import json
from pathlib import Path
from security.encryption import decrypt

def getTokensFilePath(person: str):
    """This specific path function was generated using Gemini 3.5"""
    scriptDir = Path(__file__).resolve().parent # ALWAYS resolves to T-Link/security/manageTokens.py
    return scriptDir.parent / "storage" / f"{person}Tokens.json"

def unencryptTokens(person: str):
    with open(getTokensFilePath(person), "r") as f:
        data = json.load(f)
        accessToken, refreshToken, expiresAt = data["access_token"], data["refresh_token"], data["expires_at"]
        return decrypt(accessToken), decrypt(refreshToken), expiresAt

def refreshTokens(person: str):
    print("[Refreshing token]")

if __name__ == "__main__":
    print(unencryptTokens("mom"))