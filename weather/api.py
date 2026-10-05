import requests
from weather.models import Coordinates, WeatherData

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