def calculator():
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    op=input("Enter your choice(+,-,*,/,%):")
    if op == '+':
        print("Addition is:",n1 + n2)
    elif op == '-':
        print("Subtraction is:",n1 - n2)
    elif op == '*':
        print("Multiplication is:",n1 * n2)
    elif op == '/':
        print("Division is:",n1 / n2)
    elif op == '%':
        print("modulo is:",n1 % n2)
    else:
        print("Invalid operator")
calculator()