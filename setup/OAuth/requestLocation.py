import requests

CAR_ID = "[REDACTED]"
URL = f"https://fleet-api.prd.na.vn.cloud.tesla.com/api/1/vehicles/{CAR_ID}/vehicle_data?endpoints=location_data"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer [REDACTED]"
}

r = requests.get(URL, headers=headers)
data = r.json()
print(r)
print(data)

locData = data["response"]["drive_state"]
print(f"Timestamp: {locData['timestamp']}")
print(f"Heading: {locData['heading']}")
print(f"Lat: {locData['latitude']}")
print(f"Long: {locData['longitude']}")

shiftState = locData["shift_state"]
if shiftState in ("D", "R", "N"):
    driving = True
elif (not shiftState) or (shiftState == "P"):
    driving = False
else:
    driving = None

print(f"Shift State: {shiftState} (Driving: {driving})")