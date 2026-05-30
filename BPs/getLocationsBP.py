from flask import Blueprint, request
from security.authorizeRequest import authorizeRequest

getLocationsBP = Blueprint('getLocations', __name__)

@getLocationsBP.route('/get-locations-5z592q', methods=['GET'])
def getLocations():
    data = request.get_json()
    requestKey = request.headers.get("requestKey", None)

    if not authorizeRequest(requestKey):
        return {"error": "Unauthorized"}, 401

    # 1. Use token to request for location
    # 2. Store refresh token
    # 3. Return the phone locations and the car locations

    return {"status": "success"}