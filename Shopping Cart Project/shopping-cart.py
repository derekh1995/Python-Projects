# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (\"q\" to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("----- YOUR CART -----")
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"Your total is: ${total:.2f}")

## New Shopping cart with dictionary

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")
 
while True:
    food = input("Please select an item (\"q\" to quit): ")
    if food.lower() == "q":
        # print("Goodbye.")
        break
        
    elif menu.get(food.lower()) is None:
        print("Please select a valid item")
    elif menu.get(food.lower()) is not None:
        cart.append(food.lower())
   
print("---- YOUR ORDER ----")
for food in cart:
    total += menu.get(food.lower())
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
