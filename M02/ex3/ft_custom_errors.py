class GardenError(Exception):
    default_message = "Unknown garden error"

    def __init__(self, message=None):
        super().__init__(message or self.default_message)

class PlantError(GardenError):
    default_message = "Unknown plant error"

class WaterError(GardenError):
    default_message = "Unknown water error"


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    for error in [PlantError("The tomato plant is wilting!"),
                  WaterError("Not enough water in the tank!\n")]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")

if __name__ == "__main__":
    test_custom_errors()
    print("All custom error types work correctly!")