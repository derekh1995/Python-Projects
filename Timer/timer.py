import time

# time.sleep(3)
# print("Time's up!")

input_time = int(input("Enter your time in seconds: "))

for x in range(input_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    days = int(x / 86400) % 365
    years = int(x / 31536000)
    print(f"{years}y:{days:03}d:{hours:02}h:{minutes:02}m:{seconds:02}s")
    time.sleep(1)
print("Your timer has ended!")
