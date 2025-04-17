try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError("Error")

    number = {
        "Number 1": num1,
        "Number 2": num2
    }

    print(number)
except ZeroDivisionError:
    print("number cannot be 0")
except ValueError:
    print("user cannot input other than number")