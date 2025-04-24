def fullname(**fullname):
    result = fullname.values()
    print(" ".join(result))

fullname(
    fname = "Ahmad",
    mname = "Adi",
    lname = "Wijaya"
)