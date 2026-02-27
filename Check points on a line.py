x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())
x3, y3 = map(int, input("Enter x3 y3: ").split())

if x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) == 0:
    print("All three points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")
