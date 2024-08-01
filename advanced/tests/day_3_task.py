def task_solution(number):
    if number != 0:
        if number % 2 == 0:
            return "Even"
        return "Odd"
    raise ValueError("Zero can not apply in this case")


print(task_solution(-2))

assert task_solution(2) == "Even"
assert task_solution(-1) == "Odd"
assert task_solution(1.4) == "Odd"
