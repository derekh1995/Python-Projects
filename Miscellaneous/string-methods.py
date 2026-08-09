# String Methods

# name = input("Enter your full name:\n")
# phone = input("Enter your phone number:\n")

# result = len(name)
# result = name.find(" ") # First occurrence; Returns pos. in which the queried item occurs, starting with position 0
# result = name.rfind("k") # Last occurrence; reverse find # gives "-1" if cannot find queried item
# name = name.capitalize()
# name.upper()
# name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone.count("1")
# phone = phone.replace("-", " ")

# print(phone)

# for further information:
# print(help(str))

######

username = input("Enter a username:\n")
username.find(" ")
username.isalpha()

if len(username) < 6:
    print("Your username cannot be less than 6 or more than 24 characters.")
elif len(username) > 24:
    print("Your username cannot be less than 6 or more than 24 characters.")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces.")
elif not username.isalpha():
    print("Your username cannot contain numbers.")
else:
    print(f"Welcome, {username}")
