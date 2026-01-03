def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        x = int('abc')
        print(x)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        x = 1 / 0
        print(x)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        file = open('missing.txt', 'r')
        print(file.read())
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        plants = {"flower": "rose"}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    try:
        print("Testing multiple errors together...")
        x = int('xyz')
        result = 1 / 0
        print(x, result)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
