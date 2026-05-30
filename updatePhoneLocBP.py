from flask import Blueprint, request
from security.authorizeRequest import authorizeRequest

updatePhoneLocBP = Blueprint('updatePhoneLoc', __name__)

@updatePhoneLocBP.route('/update-phone-location-9ao101', methods=['POST'])
def updatePhoneLocation():
    data = request.get_json()
    requestKey = request.headers.get("requestKey", None)

    if not authorizeRequest(requestKey):
        return {"error": "Unauthorized"}, 401

    # [Store phone location in variable]

    return {"status": "success"}