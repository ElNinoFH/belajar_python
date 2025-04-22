list = ["wafer", "ciki", "astor", "tango"]

def add_item():
    print("current list: ", list)
    new_item = input("add item: ")
    list.append(new_item)
    print("Updated shopping list: ", list)
    print(new_item)

add_item()