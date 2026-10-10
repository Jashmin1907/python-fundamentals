# Nested conditions
age = int(input("Enter age: "))

if age >= 18:
    has_id = input("Do you have an ID? (yes/no): ").strip().lower()

    if has_id == "yes":
        print("Entry permitted")
    else:
        print("ID required")
else:
    print("Entry not permitted")
