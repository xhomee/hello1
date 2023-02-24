# calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):  #множення
    return n1 * n2


def divide(n1, n2):  #ділення
    return n1 / n2

# def cal():
#     operation_symbol = input("Print operation symbol: ")
#     num2 = int(input("What is next number? "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")
#     return answer

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
def recursion():
    num1 = float(input("What is first number? "))

    for key in operations:
        print(key)

    calculat = True
    while calculat:
        operation_symbol = input("Print operation symbol: ")
        num2 = float(input("What is next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            calculat = False
            recursion()

recursion()
