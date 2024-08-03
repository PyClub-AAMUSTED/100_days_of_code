
def recursive_factorial(number:int,memo:dict):
    """A function to calculate the factorial of a number using recursion. """
    if number in (0,1):
        return 1
    elif number in memo:
        return memo[number]
    result = number * recursive_factorial(number - 1,memo)
    memo[number] = result
    return result

