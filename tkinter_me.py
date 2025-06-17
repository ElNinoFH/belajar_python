import tkinter as tk

window = tk.Tk()
window.title("My Application")
window.geometry("400x200")
window['bg'] = 'grey'

icon = tk.PhotoImage(file='python_png.png')
window.tk.call("wm", 'iconphoto', window._w, icon)

window.mainloop()