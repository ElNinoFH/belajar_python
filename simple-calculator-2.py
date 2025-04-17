def addition(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} + {num2} = {addition(num1, num2)}")
print(f"{num1} - {num2} = {substract(num1, num2)}")
print(f"{num1} x {num2} = {multiply(num1, num2)}")
print(f"{num1} : {num2} = {division(num1, num2)}")