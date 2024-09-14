def task_solution(number):
    if number != 0:
        if number % 2 == 0:
            return "Even"
        return "Odd"
    return ValueError("Zero can not apply in this case")
