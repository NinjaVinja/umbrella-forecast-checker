# ☔ Weather Umbrella Alert

A simple Python script that checks the weather forecast for the next 12 hours using the [OpenWeatherMap API](https://openweathermap.org/api) and tells you whether you should bring an umbrella.

## 📌 Objective

Print **"Bring Umbrella"** if any of the weather condition codes in the next 12-hour window are less than `700` (i.e., any form of rain, drizzle, thunderstorm, or snow).

## ⚙️ How It Works

1. Sends a request to OpenWeatherMap's **5 day / 3 hour forecast** API for a given latitude and longitude.
2. Limits the response to the next **4 forecast entries** (`cnt=4`), which cover the next **12 hours** (4 × 3-hour intervals).
3. Extracts the **weather condition ID** from the very first forecast entry and prints it.
4. Builds a list of condition codes for all 4 entries.
5. Checks if **any** code is less than `700`. If so, prints `"Bring Umbrella"`.

## 🌦️ Understanding Weather Condition Codes

OpenWeatherMap groups condition codes by range:

| Range | Group |
|-------|-------|
| 200–299 | Thunderstorm |
| 300–399 | Drizzle |
| 500–599 | Rain |
| 600–699 | Snow |
| 700–799 | Atmosphere (mist, fog, haze, etc.) |
| 800 | Clear |
| 801–804 | Clouds |

Codes below `700` indicate some form of precipitation — hence the umbrella check.

Full list: [OpenWeatherMap Weather Condition Codes](https://openweathermap.org/weather-conditions)

## 🧾 Code

```python
import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_API_KEY_HERE"
weather_params = {
    "lat": 22.973423,
    "lon": 78.656891,
    "appid": api_key,
    "cnt": 4
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
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `requests` library

```bash
pip install requests
```

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/NinjaVinja/weather-umbrella-alert.git
   cd weather-umbrella-alert
   ```

2. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

3. Replace `YOUR_API_KEY_HERE` in the script with your actual API key.

   > ⚠️ **Note:** Newly generated API keys can take up to 2 hours to activate.

4. Update the `lat` and `lon` values in `weather_params` to your desired location.

### Run

```bash
python umbrella_checker.py
```

### Sample Output

```
First forecast weather ID:  500
Condition Codes:  [500, 501, 802, 800]
Bring Umbrella
```

## 🔐 Security Note

Never commit your real API key to a public repository. Consider using environment variables instead:

```python
import os
api_key = os.environ.get("OWM_API_KEY")
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Muhammad Taha Ahmad** ([@NinjaVinja](https://github.com/NinjaVinja))
