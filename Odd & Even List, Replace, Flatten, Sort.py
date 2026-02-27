import random

# Create list of 5 odd integers
odd_list = [random.randrange(1, 50, 2) for _ in range(5)]
print("Original Odd List:", odd_list)

# Create list of 4 even integers
even_list = [random.randrange(2, 50, 2) for _ in range(4)]
print("Even List:", even_list)

# Replace third element (index 2) with even_list
odd_list[2] = even_list
print("After Replacing 3rd Element with Even List:", odd_list)

# Flatten the list
flattened_list = []
for item in odd_list:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("Flattened List:", flattened_list)

# Sort the list
flattened_list.sort()
print("Sorted List:", flattened_list)