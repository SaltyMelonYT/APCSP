class calc:
    def add(a, b):
        c = a+b
        print(c)
    def subtract(a,b):
        c = a-b
        print(c)
    def multiply(a,b):
        c = a*b
        print(c)
    def divide(a, b):
        c = a/b
        print(c)

    def doOperation():
        a = int(input("First Number: "))
        b = int(input("Second Number: "))

        operation = input("What operation to run? ").lower()
        if operation == "add" or operation == "+":
            calc.add(a, b)
        elif operation == "subtract" or operation == "sub" or operation == "-":
            calc.subtract(a, b)
        elif operation == "multiply" or operation == "x":
            calc.multiply(a, b)
        elif operation == "divide" or operation == "/":
            calc.divide(a, b)
        else:
            print("Invalid operation")

calc.doOperation()