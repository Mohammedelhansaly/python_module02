class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related errors."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related errors."""
    pass


def test_plant_error() -> None:
    """Function that raises a PlantError."""
    raise PlantError("The tomato plant is wilting!")


def test_Water_error() -> None:
    """Function that raises a WaterError."""
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    """Demonstrate custom garden error types."""
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        test_plant_error()
    except PlantError as e:
        print(f"Caught a PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        test_Water_error()
    except WaterError as e:
        print(f"Caught a WaterError: {e}")
    print("\nTesting catching all garden errors...")
    tests = [lambda:test_plant_error(), lambda:test_Water_error()]
    for test in tests:
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
