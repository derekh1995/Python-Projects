# While Loops
# Executes some code while some condition remains true

name = input("Enter your name:\n")

# if name == "":
#     print("You did not enter your name.")
# else:
#     print(f"Hello, {name}.")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name:\n")
print(f"Hello, {name}.")

food = input("Enter a food you like (q to quit):\n")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit):\n")
print("Bye. Thanks for chatting.")

num = int(input("Enter a number between 1-10:\n"))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1-10:\n"))
print(f"Your number is {num}.\n Thanks for choosing a valid number.")

##### try/except 

honor = 0

while honor < 0:
    try:
        honor = float(input("Enter character's honor level:\n))
        if honor < 0:
            print("Honor level cannot be less than zero.")
    except ValueError:
        print("Please enter a valid honor level")                        
