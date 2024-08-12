print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

try:
    option = int(input("Choose an operation: "))
    
    if option in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if option == 1:
            result = num1 + num2
            print("Result: {} + {} = {}".format(num1, num2, result))
        elif option == 2:
            result = num1 - num2
            print("Result: {} - {} = {}".format(num1, num2, result))
        elif option == 3:
            result = num1 * num2
            print("Result: {} * {} = {}".format(num1, num2, result))
        elif option == 4:
            if num2 != 0:
                result = num1 / num2
                print("Result: {} / {} = {}".format(num1, num2, result))
            else:
                print("Error: Division by zero!")
    else:
        print("Invalid operation entered")
    
except ValueError:
    print("Invalid input. Please enter a valid number.")