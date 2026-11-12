# Part 1 - My Notes Application

# 1. Write initial notes to my_notes.txt (using 'w' mode)
with open("my_notes.txt", "w") as file:
    file.write("1. Learn Python file handling.\n")
    file.write("2. Understand open, read, write, and append modes.\n")
    file.write("3. Practice exception handling.\n")

print("Initial notes written successfully.")

# 2. Append additional notes to my_notes.txt (using 'a' mode)
with open("my_notes.txt", "a") as file:
    file.write("4. Complete the week 7 assignment and push to GitHub.\n")

print("Additional notes appended successfully.")

# 3. Read and display the contents of my_notes.txt line by line (using 'r' mode)
print("\n--- Reading my_notes.txt Contents ---")
try:
    with open("my_notes.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("my_notes.txt not found.")