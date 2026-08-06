# Choose your own adventure!

print("It's 17 minutes past midnight and your headlights are the only thing between you and suffocating darkness.")
print("You look down. Your gas gauge is fast approaching empty.")
print("The dirt road you're on begins to fork, and you need to make a decision...")
direction = input("Choose a direction. (left/right): ")

if direction.lower() == "left":
    print("You take a left at the fork. You don't see the collapsed bridge before you.") 
    print("You die.")

elif direction.lower() == "right":
    print("You take a right at the fork. You continue driving and see the silhouette of a large structure in the distance.")
    print("An old manor house lies before you as your car runs out of gas. You take a deep breath, steel yourself, and exit the vehicle.")
    print("An ornate wrought iron fence spans the land as far as the eye can see.")
    gate1 = input("Do you try to open the gate, or look around the perimeter? (open/wander): ")

    if gate1.lower() == "open":
        print("The gate rattles loudly as you attempt to open it, but it doesn't budge.")
        print("If anyone is inside the house, surely they are aware that you're here now.")

    elif gate1.lower() == "wander":
        print("You decide against trying the gate and begin to look around the fenceline for any other entrances.")
        print("After about 20 minutes of walking, you notice a smaller side gate on the west side of the house is ajar.")
        gate2 = input("Do you enter? (yes/no): ")

        if gate2.lower() == "yes":
            print("You enter through the gate, being careful not to make any noise.")
            # What next?
       
        elif gate2.lower() == "no":
            print("You decide against entering.")
            # Go back to car?
            # Continue around the perimeter?
        
        else:
            print("You hesitate too long. The air leaves your lungs as something stabs you from behind.")
            print("You die.")

    else:
        print("You hesitate too long. The air leaves your lungs as something stabs you from behind.")
        print("You die.")

else:
    print("You hesitate too long. Your car runs out of gas.")
    print("You curse at your own indecisiveness as you exit the car.")
    walk1 = input("Which direction do you walk? (left/right): ")
    #if walk1.lower() == left
    #if walk1.lower() == right
    #else:
