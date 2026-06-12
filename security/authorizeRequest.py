from dotenv import load_dotenv
import os

load_dotenv()
requestKey = os.environ.get("BACKEND_REQUEST_KEY")
sampleRequestKey = os.environ.get("SAMPLE_BACKEND_REQUEST_KEY")

if not (requestKey and sampleRequestKey):
    raise Exception("Error: BACKEND_REQUEST_KEY and SAMPLE_BACKEND_REQUEST_KEY must be set in .env file")

def authorizeRequest(key):
    return key == requestKey

def authorizeSampleRequest(key):
    return key == sampleRequestKey