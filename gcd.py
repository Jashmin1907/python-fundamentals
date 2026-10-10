a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    smaller = b
else:
    smaller = a

while smaller > 0:
    if a % smaller == 0 and b % smaller == 0:
        gcd = smaller
        break
    smaller -= 1

print("The GCD of", a, "and", b, "is:", gcd)