# multiplication_table.py

# Prompt the user exactly as required
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10 (inclusive)
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
