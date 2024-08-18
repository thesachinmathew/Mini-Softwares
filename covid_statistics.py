import requests

API_URL = "https://disease.sh/v3/covid-19"

def fetch_covid_stats(region_type, region_name):
    try:
        endpoint = f"{API_URL}/{region_type}/{region_name}"
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def display_stats(data):
    if 'country' in data:
        region = data['country']
    elif 'state' in data:
        region = data['state']
    elif 'continent' in data:
        region = data['continent']
    else:
        region = "Unknown region"
    
    print(f"\nCOVID-19 Statistics for {region}:")
    print(f"Total Cases: {data['cases']}")
    print(f"Total Recoveries: {data['recovered']}")
    print(f"Total Deaths: {data['deaths']}")

def main():
    print("COVID-19 Statistics Tracker")
    region_type = input("Enter region type (countries/states/continents): ").lower()
    region_name = input(f"Enter the {region_type[:-1]} name: ").lower()

    data = fetch_covid_stats(region_type, region_name)
    
    if data:
        display_stats(data)
    else:
        print(f"Could not retrieve data for {region_name}. Please check the region name and try again.")

if __name__ == "__main__":
    main()
