s = input("Enter a string: ")

length = len(s)

print("First character:", s[0])
print("Last character:", s[length - 1])

if length % 2 != 0:
    print("Middle character:", s[length // 2])
else:
    print("No middle character (length is even)")
