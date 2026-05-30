from flask import Flask

from BPs.setupBP import setupBP
from BPs.updatePhoneLocBP import updatePhoneLocBP
from BPs.getLocationsBP import getLocationsBP

app = Flask(__name__)
app.register_blueprint(setupBP, url_prefix="/setup")
app.register_blueprint(getLocationsBP)
app.register_blueprint(updatePhoneLocBP)

if __name__ == "__main__":
    app.run(port="5000")