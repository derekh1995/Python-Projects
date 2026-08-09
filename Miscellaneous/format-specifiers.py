# Format specifiers

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 10000

print(f"Price 1 is ${price1:^+10.3f}")
print(f"Price 2 is ${price2:010.1f}")
print(f"Price 3 is ${price3:<.2f}")
print(f"Price 4 is ${price4:>,}")
