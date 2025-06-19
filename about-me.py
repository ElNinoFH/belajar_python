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

window.mainloop()