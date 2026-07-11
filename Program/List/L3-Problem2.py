list_of_numbers = []

print("Enter 10 integers:")

# Loop to ask the user for input 10 times
for i in range(10):
    # Get input, convert it to an integer, and save it to a variable
    user_input = int(input(f"Enter integer {i + 1}: "))
    
    # Add the integer to the end of our list using append()
    list_of_numbers.append(user_input)

print("Complete list:", list_of_numbers)
print("Total number of elements:", len(list_of_numbers))
