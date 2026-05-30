import requests
import json

tokenURL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"
body = {
    "grant_type": "authorization_code",
    "client_id": "[REDACTED]",
    "client_secret": "[REDACTED]",
    "code": "[REDACTED]",
    "redirect_uri": "https://friendly-waddle-wr9gvwgpg6jg3gjrx-5000.app.github.dev/setup/oauth-callback",
    "audience": "https://fleet-api.prd.na.vn.cloud.tesla.com"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

r = requests.post(tokenURL, data=body, headers=headers)
print(r)
print(r.json())