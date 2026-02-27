fahrenheit = [32, 68, 77, 104, 122]
print("Fahrenheit List:", fahrenheit)

celsius = [(temp - 32) * 5/9 for temp in fahrenheit]

print("Celsius List:", celsius)