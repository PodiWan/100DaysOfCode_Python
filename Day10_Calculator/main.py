def calculate(op1, op2, opr):
    if opr == "+":
        return op1 + op2
    elif opr == "-":
        return op1 - op2
    elif opr == "*":
        return op1 * op2
    else:
        if op2 != 0:
            return op1 / op2
        else:
            exit("Division by zero!")


def menu(carry_over):
    if carry_over == 0:
        operator1 = int(input("What's the first number?: "))
    else:
        operator1 = carry_over
    print("+\n-\n*\n/")
    operand = input("Pick an operation: ")

    if operand != "+" and operand != "-" and operand != "*" and operand != "/":
        exit("Invalid operation!")
    operator2 = int(input("What's the next number?: "))

    result = calculate(operator1, operator2, operand)
    return result

res = 0
while True:
    res = menu(res)
    cont = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")
    if cont == 'n':
        exit("Exiting...")