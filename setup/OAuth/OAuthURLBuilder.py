import urllib.parse
import secrets

baseURL = "https://auth.tesla.com/oauth2/v3/authorize"
secretString = secrets.token_hex(16)
parameters = {
    "response_type": "code",
    "client_id": "[REDACTED]",
    "redirect_uri": "https://friendly-waddle-wr9gvwgpg6jg3gjrx-5000.app.github.dev/setup/oauth-callback", # Note: MUST MATCH IN TESLA DEVELOPER DASHBOARD!
    "scope": "openid offline_access vehicle_device_data vehicle_location user_data",
    "state": secretString,
    "audience": "https://fleet-api.prd.na.vn.cloud.tesla.com",
    
    "prompt_missing_scopes": "true",
    "require_requested_scopes": "true"
}
print(f"Used Secret String: {secretString}")

URLencodedParameters = urllib.parse.urlencode(parameters)
print(f"URL: {baseURL}?{URLencodedParameters}")