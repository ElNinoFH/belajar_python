def average(*args):
    if len(args) == 0:
        return "Number cannot null"
    return sum(args) / len(args)

input_number = input("Enter a number: ")
number = [float (num) for num in input_number.split()]

result = average(*number)
print(f"Your average number is {result}")