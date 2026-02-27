# Price dictionary
prices = {
    "rice": 50,
    "wheat": 40,
    "sugar": 45
}

# Quantity dictionary
quantity = {
    "rice": 2,
    "wheat": 3,
    "sugar": 1
}

total = 0

for item in prices:
    total += prices[item] * quantity[item]

print("Total Bill =", total)
