student = {"name" : "Jaka", "address" : "Jakarta"}

car = {
    "model" : "truck",
    "brand" : "ford",
    "year" : 2010
}

print(type(student))
print(student)

print(type(car))
print(car)

print(student.keys())

print(student["name"])

print(car.keys())

print(car["brand"])

car["color"] = "red"
car["price"] = 98000
print(car)

car["year"] = 2011
car.update({"color" : ["red","black"]})
print(car)

# untuk menghapus data per key
car.pop("model")
print(car)

# untuk menghapus data terakhir
car.popitem()
print(car)