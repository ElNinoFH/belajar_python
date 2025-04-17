choice = input("Ketik pilihan anda (Ganjil/Genap): ").lower()
range_1 = int(input("Masukkan angka: "))

if choice == 'genap':
    print(f"Bilangan genap dari 0 sampai {range_1}")
    for num in range (0, range_1 + 1):
        if num % 2 == 0:
            print(num)

if choice == 'ganjil':
    print(f"Bilangan ganjil dari 0 sampai {range_1}")
    for num in range (0, range_1 + 1):
        if num % 2 != 0:
            print(num)

else:
    print("Wrong command")