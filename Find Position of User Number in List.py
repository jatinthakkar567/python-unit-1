import random

numbers = [random.randint(1, 20) for _ in range(20)]
print("Generated List:", numbers)

num = int(input("Enter number to search: "))

positions = []
for i in range(len(numbers)):
    if numbers[i] == num:
        positions.append(i)

if positions:
    print(f"{num} found at positions:", positions)
else:
    print(f"{num} not found in the list.")