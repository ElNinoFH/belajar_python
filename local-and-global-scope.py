x = "global"
def foo():
    global x
    y = "local"
    x = x * 2
    print(y)
    print(x)

foo()