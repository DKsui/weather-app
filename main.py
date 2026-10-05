from weather.api import get_weather
from weather.formatter import format_weather
from weather.validation import parse_coordinates

def main() -> None:
    print("Weather App")
    latitude_input = input("Enter latitude: ")
    longitude_input = input("Enter longitude: ")
    try:
        coordinates = parse_coordinates(latitude_input, longitude_input)
        weather = get_weather(coordinates)
    except (ValueError, RuntimeError) as error:
        print(f"Error: {error}")
        return
    print()
    print(format_weather(weather))

if __name__ == "__main__":
    main()