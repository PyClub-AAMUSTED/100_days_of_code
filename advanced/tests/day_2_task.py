def task_solution(number1, number2):
    result = number1 + number2
    return result


print(task_solution(2, 3))

assert task_solution(1, 2) == 3
assert task_solution(-1, 2) == 1
assert task_solution(1, -2) == -1
assert task_solution(2, -2) == 0
assert type(task_solution(1.4, -2)) == float
assert task_solution(0, -0) == 0
