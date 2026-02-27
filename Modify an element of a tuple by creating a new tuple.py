t = (10, 20, 30, 40)

# Modify element at index 2 (30 → 99)
new_t = t[:2] + (99,) + t[3:]

print("Original Tuple:", t)
print("Modified Tuple:", new_t)