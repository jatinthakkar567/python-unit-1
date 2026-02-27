s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1

print("Total length:", len(s))
print("Vowels:", vowels)
print("Consonants:", consonants)
