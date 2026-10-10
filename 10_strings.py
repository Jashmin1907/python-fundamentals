# String indexing, methods, and slicing
text = "PYTHON Programming"

print("First character:", text[0])
print("Last character:", text[-1])
print("Length:", len(text))
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Replace:", text.replace("Python", "Java"))
print("First three characters:", text[0:3])
print("From index 2:", text[2:])
print("Reversed:", text[::-1])

email = "  STUDENT@EXAMPLE.COM  "
print(email.strip().lower())
