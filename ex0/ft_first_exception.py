def check_temperature(temp_str) -> None:
    """Check if the given temperature string is valid for plants."""
    try:
        temp = float(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if (temp < 0):
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif (temp > 40):
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature_input() -> None:
    """Test the temperature checking function with various inputs."""
    print("=== Garden Temperature Checker ===\n")
    test_input = ["25", "abc", "100", "-50"]
    for temp in test_input:
        print("Testing temperature:", temp)
        check_temperature(temp)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
