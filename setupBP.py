from flask import Blueprint, request, jsonify

setupBP = Blueprint('setup', __name__)

@setupBP.route('/oauth-callback', methods=['POST'])
def oauthCallback():
    data = request.get_json()
    with open("oauth-callback-data.txt", "a") as f:
        f.write(str(data))