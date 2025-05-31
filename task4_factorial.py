# Q.(4) create a python function ta calculate factorial of a number using recursion.
def factorial_recursive(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Input from user
num = int(input("Enter a number to calculate its factorial: "))
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")
