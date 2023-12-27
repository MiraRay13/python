# Get user input for age
age = int(input("Enter your age: "))

# Classify the age into categories
if age <= 1:
    category = "Infant"
elif 2 <= age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
elif 20 <= age <= 64:
    category = "Adult"
else:
    category = "Senior Citizen"

# Display the result
print(f"You are classified as a {category}.")
