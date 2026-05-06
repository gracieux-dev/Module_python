def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature(temp_str: str) -> None:
    try:
        temp = input_temperature(temp_str)
        print(f"input data is '{temp}'")
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print(f"input data is '{temp_str}'")
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}'")

if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    temp_t = '25'
    temp_f = 'abc'
    test_temperature(temp_t)
    print()
    test_temperature(temp_f)
    print()
    print("All tests completed - program didn't crash!")
    