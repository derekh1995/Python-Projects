price = 0

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
if size.upper() == "S":
    price = 15
elif size.upper() == "M":
    price = 20
elif size.upper() == "L":
    price = 25
else:
    print("Please enter a valid size.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni.upper() == "Y":
    if size.upper() == "S":
        price += 2
    elif size.upper() == "M":
        price += 3
    elif size.upper() == "L":
        price += 3
    else:
        pass
elif pepperoni.upper() == "N":
    pass
else:
    print("Please enter either yes or no to pepperoni.")

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese.upper() == "Y":
    price += 1
elif extra_cheese.upper() == "N":
    pass
else:
    print("Please enter either yes or no to extra cheese.")

print(f"Your final bill is: ${price}.")
