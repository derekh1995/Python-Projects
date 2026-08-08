# Temperature conversion program

print("Welcome to my temperature converter.")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):\n")
temp = float(input("Enter the temperature:\n"))

if unit.upper() == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is:\n {temp}°F")
elif unit.upper() == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is:\n {temp}°C")
else:
    print(f"Error: \"{unit}\" is invalid!\nPlease try again with a valid unit of measurement.")
