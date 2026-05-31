import json
from pathlib import Path
from time import time
import os
import requests
from dotenv import load_dotenv

from requests.exceptions import HTTPError, RequestException
from security.encryption import decrypt, encrypt

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN_URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"

def getTokensFilePath(person: str):
    """This specific path function was generated using Gemini 3.5"""
    scriptDir = Path(__file__).resolve().parent # ALWAYS resolves to T-Link/security/manageTokens.py
    return scriptDir.parent / "storage" / f"{person}Tokens.json"

def loadTokens(person: str):
    with open(getTokensFilePath(person), "r") as f:
        data = json.load(f)
        accessToken, refreshToken, expiresAt = data["access_token"], data["refresh_token"], data["expires_at"]
        return decrypt(accessToken), decrypt(refreshToken), expiresAt

def saveTokens(person: str, accessToken, refreshToken, expiresAt):
    with open(getTokensFilePath(person), "w") as f:
        accessToken, refreshToken = encrypt(accessToken), encrypt(refreshToken)
        json.dump({
            "access_token": accessToken,
            "refresh_token": refreshToken,
            "expires_at": expiresAt
        }, f, indent=4)

def refreshTokens(person: str, refreshToken) -> tuple[str, str, None | Exception]:
    body = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refreshToken,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        r = requests.post(TOKEN_URL, data=body, headers=headers)
        r.raise_for_status()
    except (HTTPError, RequestException) as e:
        print(f"**manageTokens.py** - ERROR: Failed to refresh tokens | Error: {type(e).__name__} {e}")
        return None, None, e

    data = r.json()
    accessToken, refreshToken, expiresIn = data["access_token"], data["refresh_token"], data["expires_in"]

    expiresAt = int(expiresIn) + int(time())
    saveTokens(person, accessToken, refreshToken, expiresAt)

    return accessToken, refreshToken, None