from flask import Blueprint, request, jsonify
from security.authorizeRequest import authorizeRequest
import BPs.updatePhoneLocBP as updatePhoneLocBP

getLocationsBP = Blueprint('getLocations', __name__)

@getLocationsBP.route('/get-locations-5z592q', methods=['GET'])
def getLocations():
    requestKey = request.headers.get("requestKey", None)

    if not authorizeRequest(requestKey):
        return {"error": "Unauthorized"}, 401

    phoneLocs = updatePhoneLocBP.lastPhoneLocations

    # 1. Use token to request for location
    # 2. Store refresh token
    # 3. Return the phone locations and the car locations

    return jsonify(
        {"phoneLocations": phoneLocs}
    )