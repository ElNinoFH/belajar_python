import tkinter as tk

window = tk.Tk()
window.title("My Application")
icon = tk.PhotoImage(file='python_png.png')
window.tk.call('wm', 'iconphoto', window._w, icon)

label = tk.Label(
    text = "Hello World!",
    foreground = "white",
    background = "black",
    height = 5,
    width = 25,
    font = ("Arial", 24),
    )
label.pack()

button = tk.Button(
    text = "Blue Button",
    bg = "blue", fg = "white",
    font = ("Arial", 16),
    height = 5, width = 15
)
button.pack()

entry = tk.Entry(
    font = ("Arial", 16)
)
entry.pack()

text_box = tk.Text(
    font = ("Arial", 16),
    width = 25,
    height = 5
)
text_box.pack()

window.mainloop()