def factorial(num):
    """Function to recursively calculate the factorial of an integer"""
    if num < 2:
        return 1
    return factorial(num - 1) * num


print(factorial(5))  # 120
