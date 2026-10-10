# Lists are ordered and mutable
numbers = [10, 20, 30, 40]
print("First item:", numbers[0])

numbers.append(50)
numbers[1] = 25
numbers.remove(30)

print("Updated list:", numbers)
print("Length:", len(numbers))
print("Sum:", sum(numbers))

for number in numbers:
    print(number)
