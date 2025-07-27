# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Prompt user for input
temperature_input = input("Enter the temperature to convert: ")
try:
    temperature = float(temperature_input)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == 'C':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
elif unit == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
else:
    raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
