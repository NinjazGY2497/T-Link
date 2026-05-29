import requests

URL = "https://fleet-api.prd.na.vn.cloud.tesla.com/api/1/partner_accounts"
headers = {
    'Authorization': 'Bearer [REDACTED_PARTNER_TOKEN]',
    'Content-Type': 'application/json'
}

body = {
    "domain": "ninjazgy2497.github.io"
}

r = requests.post(URL, headers=headers, json=body)
print(r.status_code)
print(r.content)
print(r)