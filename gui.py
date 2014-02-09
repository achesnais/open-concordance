#!/usr/bin/python3

"""
    The Gui for Open Concordance. I'm still learning Tkinter...
    Copyright (C) 2014  Antoine Chesnais

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
