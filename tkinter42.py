import tkinter as tk

window = tk.Tk()
window.title("Odd or Even")

def checkNumber():
    number = int(ent_number.get())

    if number % 2 == 0:
        lbl_result['text'] = f"{number} is an even number"
    else:
        lbl_result['text'] = f"{number} is an odd number"

    ent_number.delete(0, tk.END)

lbl_title = tk.Label(
    text="Odd or Even Number Checker"
)

ent_number = tk.Entry(font=("Arial", 16))

btn_check = tk.Button(
    text="Check",
    command=checkNumber
)

lbl_result = tk.Label(font=("Arial", 16))

lbl_title.pack()
ent_number.pack()
btn_check.pack()
lbl_result.pack()

window.mainloop()