t = (10, 20, 30, 40)

# Delete element at index 1 (20)
new_t = t[:1] + t[2:]

print("Original Tuple:", t)
print("Tuple after deletion:", new_t)