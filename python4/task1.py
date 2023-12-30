def countdown(n):
    while n > 0:
        print(n)
        n -= 1

# Example usage:
countdown(5)



def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Example usage:
number = int(input("Enter a number to calculate factorial: "))
print("Factorial:", factorial(number))
