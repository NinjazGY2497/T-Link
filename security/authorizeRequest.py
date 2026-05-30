from dotenv import load_dotenv
import os

load_dotenv()
requestKey = os.environ.get("BACKEND_REQUEST_KEY")

def authorizeRequest(key):
    return key == requestKey