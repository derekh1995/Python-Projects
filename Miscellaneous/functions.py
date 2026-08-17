# Multiple practical examples of functions

# place () after function name to invoke

# def happy_birthday():
#     print("Happy birthday to you!")
#     print("Happy birthday to you!")
#     print("Happy birthday, dear user!")
#     print("Happy birthday to you!")

# happy_birthday()

# def happy_birthday(name):
#     print("Happy birthday to you!")
#     print("Happy birthday to you!")
#     print(f"Happy birthday, dear {name}!")
#     print("Happy birthday to you!")
    
# happy_birthday("John Wick")

# def happy_birthday(name, age):
#     print("Happy birthday to you!")
#     print("Happy birthday to you!")
#     print(f"Happy birthday, dear {name}!")
#     print("Happy birthday to you!")
#     print(f"Congratulations on turning {age}!")
    
# happy_birthday("John Wick", 45)

#####

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}.")
#     print(f"Your bill of ${amount:.2f} is due on {due_date}.")

# display_invoice("GWashington", 177.6, "7/4/76")

#####

# Return = statement to end function and send result back to caller

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def multiply(x, y):
#     z = x * y
#     return z
# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(9, 5))
# print(multiply(5, 5))
# print(divide(1000, 100))

#####

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("John", "Wick")

print(full_name)

