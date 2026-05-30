from datetime import datetime
from flask import Blueprint, request, jsonify

setupBP = Blueprint('setup', __name__)

def timeAndDateStr() -> str:
    now = datetime.now()
    return f"{now.strftime('%I:%M:%S %p')} {now.strftime('%m-%d-%Y')}: "

@setupBP.route('/oauth-callback')
def oauthCallback():
    data = request.args
    print(data)
    with open("setup/OAuth/oauth-callback-data.txt", "a") as f:
        f.write(timeAndDateStr() + str(data) + "\n")

    return """
        <h1>Tesla Account Connected Successfully!</h1>
        <p>You can now return back to the app.</p>
    """, 200