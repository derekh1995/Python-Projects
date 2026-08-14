# dictionary

country_capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}
# print(dir(country_capitals))
# print(help(country_capitals))

# print(country_capitals.get("USA"))

# if country_capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# country_capitals.update({"Germany": "Berlin"})
# country_capitals.update({"USA": "Manassas"})
# print(country_capitals)
# country_capitals.clear()
# country_capitals.pop("China")

# keys = country_capitals.keys()
# values = country_capitals.values()

# for key in country_capitals.keys():
#     print(key)
# for value in country_capitals.values():
#     print(value)

items = country_capitals.items()
for key, value in country_capitals.items():
    print(f"{key}: {value}")

# print(country_capitals)
