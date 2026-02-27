import random

numbers = [random.randint(-50, 50) for _ in range(30)]
print("Original List:", numbers)

positive = []
negative = []

for num in numbers:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive Numbers:", positive)
print("Negative Numbers:", negative)