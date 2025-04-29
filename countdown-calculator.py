num = int(input("Enter a number: "))

def countdown(number):
    print(number)
    if number == 0:
        return
    else:
        countdown(number -1)

result = countdown(num)
print(result)