import requests
import json

tokenURL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"
body = {
    "grant_type": "refresh_token",
    "client_id": "[REDACTED]",
    "client_secret": "[REDACTED]",
    "refresh_token": "[REDACTED]",
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(tokenURL, data=body, headers=headers)
print(response.status_code)
print(f"New Tokens: {response.json()}")