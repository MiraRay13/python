numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of numbers
numbers_list = [float(num) for num in numbers.split()]

# Initialize a variable to store the product
product = 1

# Multiply all the numbers in the list
for num in numbers_list:
    product *= num

# Display the result
print(f"The product of the numbers in the list is: {product}")
