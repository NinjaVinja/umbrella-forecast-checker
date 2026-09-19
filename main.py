import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# ==========================================================
# 🔧 EDIT THIS: paste your own OpenWeatherMap API key below
# Get one free at: https://openweathermap.org/api
# ==========================================================
api_key = "PUT_YOUR_API_KEY_HERE"

weather_params = {
    # ==========================================================
    # 🔧 EDIT THIS: set the latitude & longitude of your location
    # ==========================================================
    "lat": 22.973423,   # <-- replace with your latitude
    "lon": 78.656891,   # <-- replace with your longitude
    "appid": api_key,
    "cnt": 4             # 4 x 3-hour intervals = next 12 hours
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

first_id = data["list"][0]["weather"][0]["id"]
print("First forecast weather ID: ", first_id)

condition_codes = [entry["weather"][0]["id"] for entry in data["list"]]
print("Condition Codes: ", condition_codes)

if any(code < 700 for code in condition_codes):
    print("Bring Umbrella")
