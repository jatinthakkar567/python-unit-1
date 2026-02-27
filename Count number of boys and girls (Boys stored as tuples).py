# List containing boys (as tuples) and girls (as strings)
data = [("Rahul",), "Priya", ("Amit",), "Sneha", ("Karan",), "Pooja"]

boys = 0
girls = 0

for item in data:
    if isinstance(item, tuple):
        boys += 1
    else:
        girls += 1

print("Number of Boys:", boys)
print("Number of Girls:", girls)