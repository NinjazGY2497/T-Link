from flask import Blueprint, request
from datetime import datetime, timezone

from security.authorizeRequest import authorizeRequest
from loadSaveLocations import load, save

updatePhoneLocBP = Blueprint('updatePhoneLoc', __name__)

lastPhoneLocations = load("lastPhoneLocations")

def genTimestamp() -> int:
    utcNow = datetime.now(timezone.utc)
    return int(utcNow.timestamp())

@updatePhoneLocBP.route('/update-phone-location-9ao101', methods=['POST'])
def updatePhoneLocation():
    global lastPhoneLocations

    data = request.get_json()
    requestKey = request.headers.get("requestKey", None)

    if not authorizeRequest(requestKey):
        print(f"**updatePhoneLocBP.py** - Unauthorized request!\n")
        return {"error": "Unauthorized"}, 401

    # Process & Update
    name, lat, long = data.get("name", None), data.get("lat", None), data.get("long", None)
    if name and lat and long:
        lastPhoneLocations[name] = {
            "lat": lat,
            "long": long,
            "timestamp": genTimestamp()
        }
        save("lastPhoneLocations", lastPhoneLocations)
        print(f"**updatePhoneLocBP.py** - New updated phone locations: {lastPhoneLocations}\n")
    else:
        print(f"**updatePhoneLocBP.py** - ERROR: Invalid data: {data}\n")
        return {"error": "Invalid data"}, 400

    return {"status": "success"}, 200