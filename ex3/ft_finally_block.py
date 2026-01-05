def water_plants(plant_list) -> None:
    """Simulates watering a list of plants, ensuring cleanup
        happens regardless of errors."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests the watering system with normal and error scenarios."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    plants_with_error = ["tomato", None, "carrots"]
    water_plants(plants_with_error)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
