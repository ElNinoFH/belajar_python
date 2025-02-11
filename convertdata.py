# Cara mengubah tipe data
integer = 150
print(type(integer))

float_num = 13.6
print(type(float_num))

string = "15"
print(type(string))

# Dari integer ke string
string1 = str(integer)
print(type(string1))
print(string1)

# Dari float ke string
string2 = str(float_num)
print(type(string2))
print(string2)

# Dari string ke list
list1 = list(string)
print(type(list1))
print(list1)

# Dari integer ke float 
number1 = float(integer)
print(type(number1))
print(number1)

# Dari float ke integer
number2 = int(float_num)
print(type(number2))
print(number2)

number3 = int(string)
print(type(number3))
print(number3)