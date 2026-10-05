from weather.api import get_weather, get_location
from weather.formatter import format_weather
from weather.validation import parse_coordinates

def main() -> None:
    print("Weather App")
    print("1. Search by city")
    print("2. Search by coordinates")
    choice = input("Choose an option (1 or 2): ").strip()
    try:
        if choice == "1":
            city = input("Enter city name: ").strip()
            if not city:
                raise ValueError("City name cannot be empty.")
            location = get_location(city)
            coordinates = location.coordinates
            print(f"\nWeather for {location.name}, {location.country}")
        elif choice == "2":
            latitude_input = input("Enter latitude: ").strip()
            longitude_input = input("Enter longitude: ").strip()
            coordinates = parse_coordinates(latitude_input, longitude_input)
        else:
            raise ValueError("Invalid option. Please choose 1 or 2.")
        weather = get_weather(coordinates)
    except (ValueError, RuntimeError) as error:
        print(f"Error: {error}")
        return
    print()
    print(format_weather(weather))

if __name__ == "__main__":
    main()