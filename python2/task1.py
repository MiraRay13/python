# Get user input for a list of numbers
numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of numbers
numbers_list = [float(num) for num in numbers.split()]

# Calculate the sum of the numbers in the list
sum_of_numbers = sum(numbers_list)

# Display the result
print(f"The sum of the numbers in the list is: {sum_of_numbers}")
