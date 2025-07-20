# multiplication_table.py

#prompt the user for a number
number = int(input("Enter a number to seeit's multiplication table: "))

#loop through numbers 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
    