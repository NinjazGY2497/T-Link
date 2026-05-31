from time import time
from requests.exceptions import HTTPError, RequestException

from security.manageTokens import loadTokens, refreshTokens
from requestTeslaEndpoint import requestTeslaEndpoint

def retrieveLoc(person: str):
    accessToken, refreshToken, expiresAt = loadTokens(person)

    # --- Step 3 ---
    if time() >= expiresAt - 300: # If token will expire in 300s or less
        print("**retrieveLoc.py** - Calculated that the access token expired; refreshing...")
        accessToken, refreshToken, refreshError = refreshTokens(person, refreshToken)

        if refreshError:
            print("**retrieveLoc.py** - ERROR: Aborting retrieveLoc.py due to refresh error")
            return {"error": str(refreshError)}

        print(f"**retrieveLoc.py** - Refreshed, encrypted, and stored tokens.")

    # --- Step 4 ---
    locInfo: dict
    locError: HTTPError | RequestException | None
    locInfo, locError = requestTeslaEndpoint(person, accessToken)

    # Token Expiry or Missing Scope Perms
    if isinstance(locError, HTTPError) and locError.response.status_code in (401, 403):
        print("**retrieveLoc.py** - ERROR: Got a 401 or 403; refreshing tokens...")
        accessToken, refreshToken, refreshError = refreshTokens(person, refreshToken)

        if refreshError:
            print("**retrieveLoc.py** - ERROR: Aborting retrieveLoc.py due to refresh error")
            return {"error": str(refreshError)}

        print(f"**retrieveLoc.py** - Refreshed, encrypted, and stored tokens.")
        locInfo, locError = requestTeslaEndpoint(person, accessToken)

    # If first locError was not 401/403, OR if receiving location failed for a 2nd time
    if locError:
        # --- Pre-Step 5 --- (Catch 408 Car is Offline error)
        if isinstance(locError, HTTPError) and locError.response.status_code == 408:
            print("**retrieveLoc.py** - ERROR: Got a 408; aborting because car is offline.")
            return {"online_state": "Offline"}
        else:
            print("**retrieveLoc.py** - ERROR: Aborting retrieveLoc.py due to unknown location grabbing error")
            return {"error": str(locError)}

    print("**retrieveLoc.py** - Successfully retrieved location info.")

    return locInfo

if __name__ == "__main__":
    retrieveLoc("mom")