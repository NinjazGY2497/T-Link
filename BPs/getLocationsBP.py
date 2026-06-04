from flask import Blueprint, request, jsonify
from time import time

from security.authorizeRequest import authorizeRequest
import BPs.updatePhoneLocBP as updatePhoneLocBP
from retrieveLoc import retrieveLoc
from loadSaveLocations import load, save

getLocationsBP = Blueprint('getLocations', __name__)

lastCarLocRequest = 0 # (Timestamp)
lastCarLocations: dict = load("lastCarLocations")
locAccessHistory: dict = load("locAccessHistory")

def processCarLoc(person: str, personCarLoc: dict) -> bool: # (returns successful)
    """Updates lastCarLocations, handles errors, handles offline, and returns successful (bool)"""
    global lastCarLocations

    successful: bool = True

    if personCarLoc.get("online_state") == "Offline":
        # Offline - Use Cached Locations
        print(f"**getLocationsBP.py** - {person}'s car is offline; using cached car location")
        lastCarLocations[person]["online_state"] = "Offline"
        lastCarLocations[person]["error"] = None # (Clear any older errors)

    elif personCarLoc.get("error") is not None:
        # Error Occurred - Use Cached Locations
        print(f"**getLocationsBP.py** - ERROR: Failed to retrieve {person}'s car location")
        successful = False
        lastCarLocations[person]["error"] = personCarLoc["error"]

    else:
        # Perfect - Update Car Location
        lastCarLocations[person] = personCarLoc

    return successful

@getLocationsBP.route('/get-locations-5z592q', methods=['GET'])
def getLocations():
    global lastCarLocRequest
    global lastCarLocations
    global locAccessHistory

    requestKey = request.headers.get("requestKey", None)
    requester = request.headers.get("requester", None)

    # --- Step 1 ---
    if not authorizeRequest(requestKey):
        print(f"**getLocationsBP.py** - Unauthorized request!\n")
        return {"error": "Unauthorized"}, 401

    # --- Validate Requester ---
    if requester not in ("Mom", "Dad", "Child"):
        print(f"**getLocationsBP.py** - ERROR: Invalid requester: {requester}\n")
        return {"error": "Invalid or not found requester header"}, 401

    # --- Easy Retrieval ---
    phoneLocs = updatePhoneLocBP.lastPhoneLocations
    print(f"**getLocationsBP.py** - Retrieved phone locations: {phoneLocs}")

    # --- Save Location Access History ---
    locAccessHistory[requester] = int(time())
    save("locAccessHistory", locAccessHistory)
    print(f"**getLocationsBP.py** - Updated location access history : {locAccessHistory}")

    # --- Step 2 ---
    if time() < lastCarLocRequest + 30:
        print(f"**getLocationsBP.py** - Returning cached car locations\n")
        return jsonify({
            "status": "success",
            "phoneLocations": phoneLocs,
            "carLocations": lastCarLocations,
            "locationAccessHistory": locAccessHistory
        }), 200

    # --- Step 3 "Dispatcher" ---
    lastCarLocRequest = time()
    momCarLoc: dict = retrieveLoc("mom")
    dadCarLoc: dict = retrieveLoc("dad")

    # --- Process Car Locations ---
    momSuccess = processCarLoc("Mom", momCarLoc)
    dadSuccess = processCarLoc("Dad", dadCarLoc)
    status = "success" if (momSuccess and dadSuccess) else "error"

    print(f"**getLocationsBP.py** - Returning & saving these car locations, whether retrieval was successful or not: {lastCarLocations} | Status is: {status}\n")
    save("lastCarLocations", lastCarLocations)

    return jsonify({
        "status": status,
        "phoneLocations": phoneLocs,
        "carLocations": lastCarLocations,
        "locationAccessHistory": locAccessHistory
    }), 500 if status == "error" else 200