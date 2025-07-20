# pattern_drawing.py

# Prompt the user to enter the size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for each column in the row
    for col in range(size):
        print("*", end="")  # Print * without moving to the next line
    print()  # Move to the next line after each full row
    row += 1  # Go to the next row
