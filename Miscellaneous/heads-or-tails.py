import random

# randint = random.randint(0, 100)
# print(randint)
# import random

# import mymodule
# print(mymodule.my_favorite_number)

# random_number_0_to_1 = random.random() # you can add * 10 to make it 0-10
# print(random_number_0_to_1)

# ran_float = random.uniform(0, 10)
# print(ran_float)

ran = random.randint(0, 1)
print("Let's play!")
choice = input("Heads or tails?" )
if choice.lower() == "heads":
    print(ran)
    if ran == 1:
        print("Heads! You win!")
    elif ran == 0:
        print("Tails! You lose!")
    else:
        pass
elif choice.lower() == "tails":
    print(ran)
    if ran == 1:
        print("Heads! You lose!")
    elif ran == 0:
        print("Tails! You win!")
    else:
        pass
else:
    pass
