# Handle invalid integer input and division by zero
try:
    number = int(input("Enter an integer: "))
    print("100 divided by your number =", 100 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
