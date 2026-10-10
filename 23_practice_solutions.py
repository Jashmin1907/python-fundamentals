# Practice solutions: reverse string, character counts, prime check,
# second-largest distinct number, and a simple calculator.

from collections import Counter

# 1. Reverse a string
text = input("Enter text to reverse: ")
print("Reversed:", text[::-1])

# 2. Count character frequencies
text = input("Enter text for character counts: ")
print("Character counts:", dict(Counter(text)))

# 3. Prime number checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter an integer to check for prime: "))
print("Prime:", is_prime(number))

# 4. Second-largest distinct number
numbers = [10, 5, 20, 20, 15]
unique = sorted(set(numbers))
if len(unique) >= 2:
    print("Second-largest distinct number:", unique[-2])
else:
    print("No second-largest distinct number.")

# 5. Simple calculator
a = float(input("Calculator - first number: "))
operator = input("Operator (+, -, *, /): ").strip()
b = float(input("Calculator - second number: "))

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator.")
