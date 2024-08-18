import requests

def get_weather_data(location, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {"error": "Failed to fetch weather data"}

    data = response.json()

    # Extract the required weather data
    if "current" not in data:
        return {"error": "Invalid API response data"}

    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    return {"weather": weather, "temperature": temperature}


api_key = "e3007b97fbf44fba83240825241208"  # Replace with your WeatherAPI.com key
location = input("Enter the location (city name or coordinates): ")
weather_data = get_weather_data(location, api_key)
if "error" in weather_data:
    print(f"Error: {weather_data['error']}")
else:
    print(f"Weather: {weather_data['weather']}")
    print(f"Temperature: {weather_data['temperature']}°C")
