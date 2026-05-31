from flask import Blueprint, request, jsonify
from security.authorizeRequest import authorizeRequest
from timestamp import genTimestamp

updatePhoneLocBP = Blueprint('updatePhoneLoc', __name__)

lastPhoneLocations = {
    "Mom": {
        "lat": None,
        "long": None,
        "timestamp": None
    },
    "Dad": {
        "lat": None,
        "long": None,
        "timestamp": None
    }
}

@updatePhoneLocBP.route('/update-phone-location-9ao101', methods=['POST'])
def updatePhoneLocation():
    global lastPhoneLocations

    data = request.get_json()
    requestKey = request.headers.get("requestKey", None)

    if not authorizeRequest(requestKey):
        print(f"**updatePhoneLocBP.py** - Unauthorized request!\n")
        return {"error": "Unauthorized"}, 401

    # Process & Update
    name, long, lat = data.get("name", None), data.get("long", None), data.get("lat", None)
    if name and long and lat:
        lastPhoneLocations[name] = {
            "lat": lat,
            "long": long,
            "timestamp": genTimestamp()
        }
        print(f"**updatePhoneLocBP.py** - New updated phone locations: {lastPhoneLocations}\n")
    else:
        print(f"**updatePhoneLocBP.py** - ERROR: Invalid data: {data}\n")
        return {"error": "Invalid data"}, 400

    return {"status": "success"}