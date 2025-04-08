def addition(num1, num2):
    result = num1 + num2
    return f"{num1} + {num2} = {result}"

number = int(input("Enter a number to add: "))
loop = int(input("Enter how many loops: "))

for i in range(1,loop+1):
    print(addition(number,i))