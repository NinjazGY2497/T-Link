from flask import request, Flask

from setupBP import setupBP
from updatePhoneLocBP import updatePhoneLocBP
from getLocationsBP import getLocationsBP
from security.authorizeRequest import authorizeRequest
from security.encryption import encrypt, decrypt

app = Flask(__name__)
app.register_blueprint(setupBP, url_prefix="/setup")
app.register_blueprint(updatePhoneLocBP)
app.register_blueprint(getLocationsBP)

if __name__ == "__main__":
    app.run(port="5000")