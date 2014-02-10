#!/usr/bin/python3

"""
    A Gui for Open Concordance.
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

import tkinter as tk
from tkinter import ttk, filedialog
import corpus

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.corpus = corpus.Corpus()

    def createWidgets(self):
        
        #Menus
        #File
        self.file_button = tk.Menubutton(self, text="File", anchor=tk.W)
        self.file_button.grid(column=0, row=0)
        self.file_button.menu = tk.Menu(self.file_button, tearoff=0)
        self.file_button["menu"] = self.file_button.menu
        self.file_button.menu.add_command(label="Open Folder", command=self.corpus_load_folder)
        
        #Main Window
        self.search_expression = tk.StringVar()
        self.hits = tk.StringVar()
        self.hits.set('No search')
        ttk.Label(self, text="Concordance search:").grid(column=0, row=1, columnspan=2)
        ttk.Entry(self, textvariable=self.search_expression).grid(column=0, row=1)
        ttk.Button(self, text="Start search", command=self.concordance).grid(column=1, row=1)
        ttk.Label(self, text="Number of hits:").grid(column=0, row=2)
        ttk.Label(self, textvariable=self.hits).grid(column=1, row=2)
        
    
    def corpus_load_folder(self):
        print("Loaded")
        path = tk.filedialog.askdirectory()
        self.corpus.load_folder(path)
    
    def concordance(self):
        expr = self.search_expression.get()
        hits = self.corpus.quick_concordance(expr)
        self.hits.set(hits)

def main():
    openconc = Application()
    openconc.master.title("Open Concordance")
    openconc.mainloop()

if __name__ == "__main__":
    main()
