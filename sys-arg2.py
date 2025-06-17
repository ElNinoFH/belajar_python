import sys

arg_list = sys.argv
arg_len = len(arg_list)

ord_no = 1

print(f"Argument captured = {arg_len}")

for arg in arg_list:
    print(f"Argument {ord_no}: {arg}")
    ord_no += 1