print("YOUR SCORE")
print(f"=" * 20)

score = int(input("Masukkan angka: "))

if score > 85 and score <= 100:
    print("Grade is A")
elif score > 70 and score <= 85:
    print("Grade is B")
elif score > 50 and score <= 70:
    print("Grade is C")
elif score <= 50:
    print("Grade is D")
else:
    print("Wrong input")