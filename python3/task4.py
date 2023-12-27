# Get user input for a number representing a day of the week
day_number = int(input("Enter a number representing a day of the week (1 for Monday, 2 for Tuesday, etc.): "))

# Define a list of days
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Check if the input is within a valid range
if 1 <= day_number <= 7:
    # Print the corresponding day
    print(f"The corresponding day is {days_of_week[day_number - 1]}.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
