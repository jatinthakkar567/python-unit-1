s = input("Enter a string: ")

alphabets = 0
digits = 0

for ch in s:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
