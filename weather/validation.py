from weather.models import Coordinates

def parse_coordinates(latitude_input: str, longitude_input: str) -> Coordinates:
    try:
        latitude = float(latitude_input)
        longitude = float(longitude_input)
    except ValueError as error:
        raise ValueError("Coordinates must be numeric values.") from error
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180 degrees.")
    return Coordinates(latitude=latitude, longitude=longitude)
