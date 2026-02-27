length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("Area is greater than Perimeter")
else:
    print("Area is not greater than Perimeter")
    
print("Area =", area)
print("Perimeter =", perimeter)
