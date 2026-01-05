class GardenError(Exception):
    pass
class PlantError(GardenError):
    pass
class WaterError(GardenError):
    pass
class HealthError(GardenError):
    pass
class Plant:
    def __init__(self,name,water_level, sunlight_hours):
        
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

class GardenManager:
    plants = []
    water_tank = 10
    @classmethod
    def add_plant(cls, plant) -> None:
        try:
            if not isinstance(plant.name, str) or plant.name == "":
                raise PlantError("Plant name cannot be empty")
            cls.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    @classmethod
    def water_plants(cls) -> None:
        print("Watering plants...")
        print("Opening watering system")
        try:
            if cls.water_tank <= 0:
                raise WaterError("Not enough water in tank")
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
    def check_plant_health(cls):
        try:
            for plant in cls.plants:
                if plant.name is None:
                    raise HealthError("Plant name cannot be empty!")
                elif plant.water_level < 1 or plant.water_level > 10:
                    raise HealthError(f"Water level {plant.water_level} is too high (max 10)")
                elif plant.sunlight_hours < 2 or plant.sunlight_hours > 12:
                    raise HealthError(f"Sunlight hours {plant.sunlight_hours}"
                                    f" is too low (min 2)")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})")
        except HealthError as e:
            print(f"Error checking {plant.name}: {e}")


if __name__ == "__main__":
    garden_manager = GardenManager()
    print("Adding plants to garden...")
    tomato = Plant("tomate", 5, 8)
    lettuce = Plant("lettuce", 15, 4)
    rose = Plant("", 3, 4)


    garden_manager.add_plant(tomato)
    garden_manager.add_plant(lettuce)
    garden_manager.add_plant(rose)
    print()
    garden_manager.water_plants()
    print()
    print("Checking plant health...")
    garden_manager.check_plant_health()
    print()
    print("Testing error recovery...")
    garden_manager.water_tank = 0
    try:
        garden_manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")