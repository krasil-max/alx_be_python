num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
operation = input('Choose the operation (+, -, *, /):')
match operation :
    case "+":
        result = num1 + num2
        print(f'The result is {result}.')
    case "-":
        result = num1 - num2
        print(f'The result is {result}.')
    case "*":
        result = num1 * num2
        print(f'The result is {result}.')
    case "/":
        result = num1 / num2
        if num2 == 0:
            print('invalid num2. Please enter again')
        else:
            print(f'The result is {result}.')
    case _:
        print("Invalid operation! Please choose one of +, -, *, or /.")