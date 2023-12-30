def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 4 == 0 and i % 7 == 0:
            print("FizzBuzz")
        elif i % 4 == 0:
            print("Fizz")
        elif i % 7 == 0:
            print("Buzz")
        else:
            print(i)

# Taking input from the user
user_input = int(input("Enter a number (n): "))
fizzbuzz(user_input)
