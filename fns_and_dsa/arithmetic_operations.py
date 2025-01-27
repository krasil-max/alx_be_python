def perform_operation(argOne,argTwo,op):
    num1 = argOne
    num2 = argTwo
    operation = op
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return ('num1 not divisible by num2')
        return num1 / num2
    else:
        return 'invalid input'
            
