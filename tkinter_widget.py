import tkinter as tk

window = tk.Tk()
window.title("My Application")
icon = tk.PhotoImage(file='python_png.png')
window.tk.call('wm', 'iconphoto', window._w, icon)

# label = tk.Label(
#     text = "Hello World!",
#     foreground = "white",
#     background = "black",
#     height = 5,
#     width = 25,
#     font = ("Arial", 24),
#     )
# label.pack()

# button = tk.Button(
#     text = "Blue Button",
#     bg = "blue", fg = "white",
#     font = ("Arial", 16),
#     height = 5, width = 15
# )
# button.pack()

# entry = tk.Entry(
#     font = ("Arial", 16)
# )
# entry.pack()

# text_box = tk.Text(
#     font = ("Arial", 16),
#     width = 25,
#     height = 5
# )
# text_box.pack()

# frame_title = tk.Frame(
#     master = window,
#     height = 100,
#     bg = "blue"
# )

frame_title = tk.Frame(
    width = 250,
    bg = "green"
)

frame_desc = tk.Frame(
    width = 150,
    bg = "blue"
)

# frame_desc = tk.Frame(
#     master = window,
#     height = 50, width = 250,
#     bg = "red"
# )

# label_title = tk.Label(
#     master = frame_title,
#     text ="My Application",
#     font = ("Arial", 25),
# )
# label_title.pack()

# label_desc = tk.Label(
#     master = frame_desc,
#     text = "Descriptions here",
#     )

# label_desc.pack()



frame_title.pack(fill = tk.Y, side = tk.LEFT)
frame_desc.pack(fill = tk.Y, side = tk.LEFT)

window.mainloop()