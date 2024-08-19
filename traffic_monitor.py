import requests
import json
import time
from datetime import datetime, timedelta

def get_traffic_data(origin, destination):
    """Fetches traffic data using Google Maps Distance Matrix API"""
    api_key = "GAPI-KEY"  # Replace with your API key
    departure_time = int((datetime.now() + timedelta(minutes=5)).timestamp())
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&departure_time={departure_time}&traffic_model=best_guess&key={api_key}" 

    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    return data

def process_traffic_data(data):
    """Processes the API response to extract traffic information"""
    distance = data['rows'][0]['elements'][0]['distance']['text']
    duration = data['rows'][0]['elements'][0]['duration']['text']
    traffic_status = data['rows'][0]['elements'][0]['status']
    return distance, duration, traffic_status

def main():
    origin = "Bangalore"
    destination = "Mysore"

    try:
        while True:
            traffic_data = get_traffic_data(origin, destination)
            distance, duration, traffic_status = process_traffic_data(traffic_data)
            print(f"Distance: {distance}")
            print(f"Duration: {duration}")
            print(f"Traffic Status: {traffic_status}")
            time.sleep(60)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
  main()
