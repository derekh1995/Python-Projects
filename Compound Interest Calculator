# Compound Interest Calculator

# A = P(1 + (r/n))^t
# A = Final Amount
# P = Initial Principle Balance
# r = Interest Rate (as decimal)
# n = Compounding periods per year
# t = Time in years

principle = 0
rate = 0
time = 0

while principle <= 0:
    try:
        principle = float(input("Enter your principle amount:\n"))
        if principle <= 0:
            print("Principle cannot be less than or equal to zero.")
    except ValueError:
        print("Please enter a valid principle.")

while rate <= 0:
    try:
        rate = float(input("Enter your interest rate:\n"))
        if rate <= 0:
            print("Interest rate cannot be less than or equal to zero.")
    except ValueError:
        print("Please enter a valid rate.")

while time <= 0:
    try:
        time = float(input("Enter your time in years:\n"))
        if time <= 0:
            print("Time cannot be less than or equal to zero.")
    except ValueError:
        print("Please enter a valid time.")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year(s): ${total:,.2f}")
