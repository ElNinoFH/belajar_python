import hashlib

mypassword = "password123"
encodedPassword = mypassword.encode('utf-8')

hashedPassword = hashlib.md5(encodedPassword).hexdigest()

print(hashedPassword)