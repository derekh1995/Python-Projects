# Weight converter (Kg/Lbs)

print("Welcome to my weight converter.")
weight = float(input("Please enter your weight: "))
unit = input("Kilograms or Pounds (kgs or lbs): ")

if unit.lower() == "kgs":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight in pounds is: {round(weight, 1)} {unit}")
elif unit.lower() == "lbs":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight in kilograms is: {round(weight, 1)} {unit}")
else:
    print(f"Error: \"{unit}\" is not a valid unit.\nPlease try again with a valid weight unit.")
