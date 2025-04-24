# def addition (a, b):
#     add = a + b
#     result = f"{a} + {b} = {add}"
#     print(result)

# addition(15, 10, 11)

def addition(*numbers):
    result = 0
    for num in numbers:
        result += num
    
    print(result)

addition(1,2,3,4,5,6,7)