number = int(input("Enter a number: "))

def hitung(num):
    if num <= 1:
        return 1
    else:
        result = num * hitung(num - 1)
        return result

factorial = hitung(number)
print(f"Faktorial dari {number} adalah {factorial}")