n = int(input("Enter n: "))
r = int(input("Enter r: "))

# factorial
def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

nCr = fact(n) // (fact(r) * fact(n-r))
nPr = fact(n) // fact(n-r)

print("nCr =", nCr)
print("nPr =", nPr)
