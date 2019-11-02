# location.py

from uszipcode import SearchEngine
import requests

API_KEY = 'dc5ea0e10f11465f9ea0e10f11e65fa6'

def get_location_coords(zipcode):
    search = SearchEngine(simple_zipcode=True)
    data = search.by_zipcode(zipcode)
    data = data.to_json()
    coords = [data["lat"], data["long"]]
    return coords

def get_weather_alert(zipcode):
    location = get_location_coords(zipcode)
    coordinates = location[0] + ',' + location[1]
    alert_url = 'https://api.weather.com/v3/alerts/headlines'
    params = {'geocode': coordinates, 'format': 'json', 'Accept-Encoding': 'gzip'}
    weather_response = requests.get(alert_url, params=params).json()
    return weather_response




