weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = weight_kg / (height_m ** 2)

print(f"Your Body Mass Index (BMI) is: {bmi}")
