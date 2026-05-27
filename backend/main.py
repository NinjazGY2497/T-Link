from flask import request, Flask
from security.authorizeRequest import authorizeRequest
from security.encryption import encrypt, decrypt

app = Flask(__name__)

@app.route('/update-phone-location-9ao101', methods=['POST'])
def updatePhoneLocation():
    data = request.get_json()
    requestKey = data.get("requestKey")
    
    if not authorizeRequest(requestKey):
        return {"error": "Unauthorized"}, 401
    
    # [Store phone location in variable]
    
    return {"status": "success"}

@app.route('/get-locations-5z592q')
def getLocations():
    data = request.get_json()
    requestKey = data.get("requestKey")
    
    if not authorizeRequest(requestKey):
        return {"error": "Unauthorized"}, 401

    # 1. Use token to request for location
    # 2. Store refresh token
    # 3. Return the phone locations and the car locations

    return {"status": "success"}