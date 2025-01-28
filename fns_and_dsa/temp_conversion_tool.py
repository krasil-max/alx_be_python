FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter temperature: "))  
        unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").strip().lower()

        if unit == "c" or unit == "celsius":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {fahrenheit:.2f}°F.")
        elif unit == "f" or unit == "fahrenheit":
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {celsius:.2f}°C.")
        else:
            print("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
         print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
