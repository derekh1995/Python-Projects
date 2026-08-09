# Nested Loops
import time

# for x in range(5):
#     time.sleep(0.5)
#     for y in range(1, 10):
#         print(y, end="")
#     print()

love = input("Do you love me? (yes/no): ")
if love.lower() == "yes":
    for x in range(10):
        time.sleep(0.5)
        for y in "I love you too!!!\n":
            print(y, end="")
    print()
elif love.lower() == "no":
    for x in range(10):
        time.sleep(0.5)
        for y in "I still love you though :(\n":
            print(y, end="")
    print()
else:
    print("Please say \"yes\" or \"no\"!")
