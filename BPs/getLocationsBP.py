from flask import Blueprint, request, jsonify
from time import time

from security.authorizeRequest import authorizeRequest
import BPs.updatePhoneLocBP as updatePhoneLocBP
from retrieveLoc import retrieveLoc

getLocationsBP = Blueprint('getLocations', __name__)

lastCarLocRequest = 0 # (Timestamp)
lastCarLocations: dict = {
    "Mom": {
        "latitude": None,
        "longitude": None,
        "heading": None,
        "timestamp": None,
        "driving_state": None, # (shift_state)
        "online_state": None
    },
    "Dad": {
        "latitude": None,
        "longitude": None,
        "heading": None,
        "timestamp": None,
        "driving_state": None, # (shift_state)
        "online_state": None
    }
}

@getLocationsBP.route('/get-locations-5z592q', methods=['GET'])
def getLocations():
    global lastCarLocRequest

    requestKey = request.headers.get("requestKey", None)

    # --- Step 1 ---
    if not authorizeRequest(requestKey):
        print(f"**getLocationsBP.py** - Unauthorized request!")
        return {"error": "Unauthorized"}, 401

    # --- Easy Retrieval ---
    phoneLocs = updatePhoneLocBP.lastPhoneLocations
    print(f"**getLocationsBP.py** - Retrieved phone locations: {phoneLocs}")

    # --- Step 2 ---
    if time() < lastCarLocRequest + 30:
        print(f"**getLocationsBP.py** - Returning cached car locations")
        return jsonify({
            "status": "cached",
            "phoneLocations": phoneLocs,
            "carLocations": lastCarLocations
        })

    lastCarLocRequest = time()
    momCarLoc: dict = retrieveLoc("mom")
    dadCarLoc: dict = retrieveLoc("dad")
    status = "updated"

    if "error" in momCarLoc:
        print(f"**getLocationsBP.py** - ERROR: Failed to retrieve Mom's car location")
        status = "error"
    else:
        lastCarLocations["Mom"] = momCarLoc # Update cache

    if "error" in dadCarLoc:
        print(f"**getLocationsBP.py** - ERROR: Failed to retrieve Dad's car location")
        status = "error"
    else:
        lastCarLocations["Dad"] = dadCarLoc # Update cache

    print(f"**getLocationsBP.py** - Returning these car locations, whether retrieval was successful or not: {lastCarLocations}")
    return jsonify({
        "status": status,
        "phoneLocations": phoneLocs,
        "carLocations": lastCarLocations,
    })