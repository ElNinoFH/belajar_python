print("COMPARING NUMBER")
print(f"=" * 15)

num1 = input("Masukkan angka pertama: ")
operator = input(" ")
num2 = input("Masukkan angka kedua: ")
rumus = f"{num1} {operator} {num2}"
hasil = eval(rumus)

print(f"{num1} {operator} {num2} = {hasil}")