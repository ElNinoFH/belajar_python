class Student:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getPhone(self):
        return self.phone
    
    def welcome_message(self):
        return f"Welcome {self.name}! Your address is {self.address} and your phone number is {self.phone}."

name = input("Enter your name: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")

object1 = Student(name, address, phone)

print(object1.welcome_message())