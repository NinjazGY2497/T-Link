from flask import Blueprint, request, jsonify

setupBP = Blueprint('setup', __name__)

@setupBP.route('/oauth-callback')
def oauthCallback():
    data = request.args
    print(data)
    with open("storage/oauth-callback-data.txt", "a") as f:
        f.write(str(data) + "\n")

    return """
        <h1>Tesla Account Connected Successfully!</h1>
        <p>You can now return back to the app.</p>
    """, 200