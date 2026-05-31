from dotenv import load_dotenv
import requests
from requests.exceptions import HTTPError, RequestException
import os

load_dotenv()
personToURL: dict = {
    "mom": f"https://fleet-api.prd.na.vn.cloud.tesla.com/api/1/vehicles/{os.getenv('MOM_CAR_ID')}/vehicle_data?endpoints=location_data",
    "dad": f"https://fleet-api.prd.na.vn.cloud.tesla.com/api/1/vehicles/{os.getenv('DAD_CAR_ID')}/vehicle_data?endpoints=location_data"
}

def requestTeslaEndpoint(person: str, accessToken) -> tuple[dict, Exception | None]:
    URL = personToURL[person]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {accessToken}"
    }
    try:
        r = requests.get(URL, headers=headers)
        r.raise_for_status()
    except (HTTPError, RequestException) as e:
        print(f"**requestTeslaEndpoint.py** - ERROR: Failed to request Tesla location endpoint | Error: {type(e).__name__} {e}")
        return None, e

    locData = r.json()["response"]["drive_state"]

    shiftState = locData.get("shift_state")
    isDriving: bool = False
    if shiftState in ("D", "R", "N"):
        isDriving = True
    elif (not shiftState) or (shiftState == "P"):
        isDriving = False

    return {
        "latitude": locData["latitude"],
        "longitude": locData["longitude"],
        "heading": locData["heading"],
        "timestamp": locData["timestamp"] / 1000,
        "driving_state": "Driving" if isDriving else "Parked",
        "online_state": "Online",
        "error": None
    }, None