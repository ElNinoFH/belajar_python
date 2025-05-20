# import mymodule as mm

# mm.greeting("malik")
# msg = "A module author is "+mm.author
# print(msg)

from mymodule import greeting, author

greeting("malik")

msg = "A module author is "+author
print(msg)