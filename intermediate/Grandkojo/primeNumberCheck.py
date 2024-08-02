def prime_number_check(number: int) -> str:
    """ This function checks if a number is a prime number
    """
    if not isinstance(number, int) or number <=1:
        return "Invalid"
    
    if number == 2:
        return "Prime Number"

    if number % 2 == 0:
        return "Not a prime number"
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return "Not a prime number"
    return "Prime Number"