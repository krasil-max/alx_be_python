
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 + 32

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return (celsius * (9/5)) + 32

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return (fahrenheit - 32) * (5/9)

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

            if unit == 'C':
                converted_temp = celsius_to_fahrenheit(temperature)
                print(f"{temperature:.2f}°C is equal to {converted_temp:.2f}°F")
            elif unit == 'F':
                converted_temp = fahrenheit_to_celsius(temperature)
                print(f"{temperature:.2f}°F is equal to {converted_temp:.2f}°C")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue 

        except ValueError:
            print("Invalid input. Please enter a numeric value for the temperature.")

        break 

if '_name_' == "_main_":
    main()
