variable1 = input("Enter the value for variable1: ")
variable2 = input("Enter the value for variable2: ")

print(f"Before swapping: variable1 = {variable1}, variable2 = {variable2}")

variable1, variable2 = variable2, variable1

print(f"After swapping: variable1 = {variable1}, variable2 = {variable2}")
