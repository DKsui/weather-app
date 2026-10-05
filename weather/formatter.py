from weather.models import WeatherData

def format_weather(weather: WeatherData) -> str:
    return(
        f"Temperature: {weather.temperature}°C\n"
        f"Feels like: {weather.feels_like}°C\n"
        f"Humidity: {weather.humidity}%\n"
        f"Wind speed: {weather.wind_speed} km/h"
    )