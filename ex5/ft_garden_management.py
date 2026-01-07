class GardenError(Exception):
    """Base class for garden management errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related errors."""
    pass


class WaterError(GardenError):
    """Exception raised for watering-related errors."""
    pass


class HealthError(GardenError):
    """Exception raised for plant health-related errors."""
    pass


class Plant:
    """Class representing a plant in the garden."""
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Class to manage garden operations."""
    plants = []
    water_tank = 10

    @classmethod
    def add_plant(cls, plant) -> None:
        """Add a plant to the garden."""
        try:
            if not isinstance(plant.name, str) or plant.name == "":
                raise PlantError("Plant name cannot be empty")
            cls.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    @classmethod
    def water_plants(cls) -> None:
        """Water all plants in the garden."""
        try:
            print("Watering plants...")
            print("Opening watering system")
            for plant in cls.plants:
                if not isinstance(plant.name, str):
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant.name} - success")
                plant.water_level += 1
                cls.water_tank -= 1
        except WaterError as e:
            raise GardenError(e)
        finally:
            print("Closing watering system (cleanup)")

    @classmethod
    def check_plant_health(cls) -> None:
        """Check the health of all plants in the garden."""
        try:
            for plant in cls.plants:
                if plant.name is None:
                    raise HealthError("Plant name cannot be empty!")
                elif plant.water_level < 1 or plant.water_level > 10:
                    raise HealthError(f"Water level {plant.water_level}"
                                      f" is too high (max 10)")
                elif (plant.sunlight_hours < 2 or
                      plant.sunlight_hours > 12):
                    raise HealthError(f"Sunlight hours {plant.sunlight_hours}"
                                      f" is too low (min 2)")
                else:
                    print(f"{plant.name}: healthy (water: "
                          f"{plant.water_level}, sun: {plant.sunlight_hours})")
        except HealthError as e:
            print(f"Error checking {plant.name}: {e}")


if __name__ == "__main__":
    print("Adding plants to garden...")
    tomato = Plant("tomate", 4, 8)
    lettuce = Plant("lettuce", 14, 4)
    rose = Plant("", 3, 4)
    GardenManager.add_plant(tomato)
    GardenManager.add_plant(lettuce)
    GardenManager.add_plant(rose)
    print()
    try:
        GardenManager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()
    print("Checking plant health...")
    GardenManager.check_plant_health()
    print()
    GardenManager.water_tank = 0
    print("Testing error recovery...")
    try:
        if GardenManager.water_tank <= 0:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
