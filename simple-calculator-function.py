def addition(num1, num2):
    result = num1 + num2
    return f"{num1} + {num2} = {result}"

def substract(num1, num2):
    result = num1 - num2
    return f"{num1} - {num2} = {result}"

def multiply(num1, num2):
    result = num1 * num2
    return f"{num1} x {num2} = {result}"

def division(num1, num2):
    result = num1 / num2
    return f"{num1} : {num2} = {result}"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(addition(num1, num2))
print(substract(num1, num2))
print(multiply(num1, num2))
print(division(num1, num2))