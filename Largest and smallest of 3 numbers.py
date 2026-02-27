a=float(input("Enter number 1: "))
b=float(input("Enter number 2: "))
c=float(input("Enter number 3: "))

largest = a
smallest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
if b < smallest:
    smallest = b    
if c < smallest:
    smallest = c

print("Largest is:", largest)
print("Smallest is:", smallest)   