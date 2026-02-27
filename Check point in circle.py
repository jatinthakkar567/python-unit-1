import math

x, y = map(float, input("Enter center coordinates (x y): ").split())
r = float(input("Enter radius: "))

x1, y1 = map(float, input("Enter point coordinates (x1 y1): ").split())

d = math.sqrt(math.pow(x1 - x, 2) + math.pow(y1 - y, 2))

if d < r:
    print("The point lies inside the circle.")
elif d == r:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")
