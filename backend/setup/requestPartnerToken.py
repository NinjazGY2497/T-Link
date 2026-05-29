import requests

URL = "https://fleet-auth.prd.vn.cloud.tesla.com/oauth2/v3/token"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
body = {
    'grant_type': 'client_credentials',
    'client_id': '[REDACTED]',
    'client_secret': '[REDACTED]',
    'scope': 'openid'
}

r = requests.post(URL, headers=headers, data=body)
print(r.content)