def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp >= 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp

def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature('25')
    print()
    test_temperature('abc')
    print()
    test_temperature('100')
    print()
    test_temperature('-50')
    print()
    print("All tests completed - program didn't crash!")