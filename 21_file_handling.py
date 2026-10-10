# Write to and read from a text file
# Running this script creates notes.txt in the current directory.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
