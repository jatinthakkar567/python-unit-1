num = int(input("Enter a number: "))

# Prime
if num > 1:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
else:
    prime = False

print("Prime:", prime)

# Perfect
sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i
print("Perfect:", sum_div == num)

# Armstrong
temp = num
digits = len(str(num))
sum_arm = 0
while temp > 0:
    digit = temp % 10
    sum_arm += digit ** digits
    temp //= 10
print("Armstrong:", sum_arm == num)

# Palindrome
print("Palindrome:", str(num) == str(num)[::-1])

# Automorphic
square = num * num
print("Automorphic:", str(square).endswith(str(num)))
