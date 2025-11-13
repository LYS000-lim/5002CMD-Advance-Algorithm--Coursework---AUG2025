def factorial(n):
    """
    Calculate factorial of a given number n.
    """
    result = 1
    for i in range(1, n + 1):  # loop runs n times
        result *= i
    return result

print(f"Factorial of 3 is: {factorial(3)}")
