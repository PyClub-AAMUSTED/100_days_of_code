# wite your code here
"""Task 1"""
import math

def check_prime_number(number:int)->bool:
    """Function to check if a number is prime or not
    Args: 
        number: int
    Returns: bool
    """
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(number)),2):
        if number % i == 0:
            return False
    return True

