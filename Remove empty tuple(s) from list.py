tuples_list = [(), (1, 2), (), ("A",), (3, 4, 5), ()]

# Removing empty tuples
new_list = [t for t in tuples_list if t]

print("List after removing empty tuples:")
print(new_list)