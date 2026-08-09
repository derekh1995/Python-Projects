# For Loops
# Executes a block of code a fixed number of times

for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!")

for x in range(1, 11, 2):
    print(x)

msg = "I love you"
for x in msg:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue # skips 13
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break # stops the script before printing 13
    else:
        print(x)
