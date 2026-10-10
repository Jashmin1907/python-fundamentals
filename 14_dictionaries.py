# Dictionaries store key-value pairs
student = {
    "name": "Ram",
    "age": 20,
    "marks": 85,
}

print("Name:", student["name"])
print("Marks:", student["marks"])

student["marks"] = 90
student["city"] = "Bhimavaram"
print("Updated record:", student)

for key, value in student.items():
    print(key, ":", value)
