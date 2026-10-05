from dataclasses import dataclass

@dataclass
class Coordinates:
    latitude: float
    longitude: float

@dataclass
class WeatherData:
    temperature: float
    feels_like: float
    humidity: float
    wind_speed: float

@dataclass
class Location:
    name: str
    country: str
    coordinates: Coordinates