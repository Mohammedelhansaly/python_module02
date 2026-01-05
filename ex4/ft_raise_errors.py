def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    try:
        if plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        elif water_level < 1 or water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f" is too low (min 2)")
        else:
            return f"Plant '{plant_name}' is healthy!"
    except ValueError as e:
        return f"Error: {e}"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    print(check_plant_health("tomato", 5, 6))
    print()
    print("Testing empty plant name...")
    print(check_plant_health(None, 5, 6))
    print()
    print("Testing bad water level...")
    print(check_plant_health("lettuce", 20, 6))
    print()
    print("Testing bad sunlight hours...")
    print(check_plant_health("carrots", 5, 0))
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
