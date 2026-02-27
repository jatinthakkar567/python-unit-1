# List of tuples (food_item, price)
food = [
    ("Pizza", 250),
    ("Burger", 120),
    ("Pasta", 180),
    ("Sandwich", 90)
]

# Sorting by price (index 1) in descending order
sorted_food = sorted(food, key=lambda x: x[1], reverse=True)

print("Sorted Food Items (Descending by Price):")
for item in sorted_food:
    print(item)