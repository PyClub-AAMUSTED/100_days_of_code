
def calculator():
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))
        summ = num1 + num2
        print(f"The sum is {summ}")
        difference = num1 - num2
        print(f"The difference is {difference}")
        multiplication = num1 * num2
        print(f"The product is {multiplication}")
        division = num1/num2
        print(f"The quotient is {division}")
        return 0
calculator()