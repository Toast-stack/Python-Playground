from urllib import response
import requests
import json
from config import API_KEY, BASE_URL

def fetch_nasa_data(endpoint, filename="nasa_data.json"):
    """Fetch live data from NASA API and save as JSON."""
    url = f"{BASE_URL}{endpoint}?api_key={API_KEY}&start_date=2025-05-01&end_date=2025-05-15"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None