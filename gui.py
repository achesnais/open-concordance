from tkinter import *
from tkinter import ttk
root = Tk()
root.option_add("*tearOff", False)
main_window = ttk.Frame(root).grid(column=0, row=0)
menu_bar = Menu(main_window)
menu_file = Menu(menu_bar)
menu_bar.add_cascade(menu=menu_file, label='File')
ttk.Label(main_window, text="Hello everyone!").grid(column=1, row=1)
root.mainloop()
