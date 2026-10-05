import requests
from weather.models import Coordinates, WeatherData, Location

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
BASE_URL = "https://api.open-meteo.com/v1/forecast"
def get_weather(coordinates: Coordinates) -> WeatherData:
    params = {
        "latitude": coordinates.latitude,
        "longitude": coordinates.longitude,
        "current": (
            "temperature_2m,"
            "apparent_temperature,"
            "relative_humidity_2m,"
            "wind_speed_10m"
        ),
    }
    try:
        response = requests.get(BASE_URL, params = params, timeout = 10)
        response.raise_for_status()
    except requests.RequestException as error:
        raise RuntimeError("Could not retrieve weather data.") from error
    try:
        data = response.json()
        current = data["current"]
        return WeatherData(
            temperature = current["temperature_2m"],
            feels_like = current["apparent_temperature"],
            humidity = current["relative_humidity_2m"],
            wind_speed = current["wind_speed_10m"],
        )
    except (KeyError, TypeError, ValueError) as error:
        raise RuntimeError("Weather API returned unexpected data.") from error

def get_location(city: str) -> Location:
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }
    try:
        response = requests.get(
            GEOCODING_URL,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise RuntimeError("Could not retrieve location data.") from error
    try:
        data = response.json()
    except (KeyError, TypeError, ValueError) as error:
        raise RuntimeError("Geocoding API returned unexpected data.") from error
    results = data.get("results", [])
    if not results:
        raise ValueError(f"City not found: {city}")
    location_data = results[0]
    try:
        return Location(
            name=location_data["name"],
            country=location_data["country"],
            coordinates=Coordinates(
                latitude=location_data["latitude"],
                longitude=location_data["longitude"],
            ),
        )
    except (KeyError, TypeError) as error:
        raise RuntimeError("Geocoding API returned unexpected data.") from error