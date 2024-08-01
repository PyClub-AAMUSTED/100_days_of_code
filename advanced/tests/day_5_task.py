def task_solution(n):
    a = 0
    b = 1
    seq = [a, b]

    if n < 0:
        return "Invalid number"
    if n == 0:
        return seq[0]
    if n == 1:
        return seq[1]
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        seq.append(b)
    return seq
