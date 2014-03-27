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

import time
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
        self.menu_bar = tk.Frame(self)
        self.menu_bar.grid(row=0, sticky=tk.W)
        
            #File
        self.file_button = tk.Menubutton(self.menu_bar, text="File")
        self.file_button.grid(column=0, row=0)
        self.file_button.menu = tk.Menu(self.file_button, tearoff=0)
        self.file_button["menu"] = self.file_button.menu
        self.file_button.menu.add_command(label="Open Folder", command=self.corpus_load_folder)
        
        #Output area
        self.output_window = tk.Frame(self)
        self.output_window.grid(column=0, row=1)
        self.output_window.columnconfigure(0, weight=1)
            #Text area
        self.concordance_output = tk.StringVar()
        self.conc_output_area = tk.Text(self.output_window, wrap=tk.NONE)
        self.conc_output_area.grid(column=0, row=0, columnspan=4)
        self.conc_output_area.insert(tk.END, "Output here!")
        self.conc_output_area.configure(state="disabled")
            #Vertical scrollbar
        self.output_window.xscrollbar = tk.Scrollbar(self.output_window, orient=tk.HORIZONTAL, command=self.conc_output_area.xview)
        self.output_window.xscrollbar.grid(column=0, row=2, sticky=tk.W+tk.E)
        self.conc_output_area["xscrollcommand"] = self.output_window.xscrollbar.set
        
        #Command bar
        self.command_window = tk.Frame(self)
        self.command_window.grid(column=0, row=2)
        self.search_expression = tk.StringVar()
        self.hits = tk.StringVar()
        self.hits.set('No search')
        ttk.Label(self.command_window, text="Concordance search:").grid(column=1, row=1)
        ttk.Entry(self.command_window, textvariable=self.search_expression).grid(column=1, row=2)
        ttk.Button(self.command_window, text="Start search", command=self.concordance).grid(column=2, row=2)
        ttk.Label(self.command_window, text="Number of hits:").grid(column=1, row=3)
        ttk.Label(self.command_window, textvariable=self.hits).grid(column=2, row=3)
            
        
    
    def corpus_load_folder(self):
        path = filedialog.askdirectory()
        self.corpus.load_folder(path)
    
    def concordance(self):
        t = time.time()
        expr = self.search_expression.get()
        hits = self.corpus.quick_concordance(expr)
        hits, results = self.corpus.concordance(expr, output="std")
        self.hits.set(hits)
        self.clear_text_area()
        self.conc_output_area.configure(state="normal")
        l_width = r_width = p_width = 0
        w_width = len(expr)
        for r in results:
            l_width = max(l_width, len(r[1]))
            r_width = max(r_width, len(r[2]))
            p_width = max(p_width, len(r[3]))
        for r in results:
            self.conc_output_area.insert(tk.END, "{0:>{lw}} <{1:^{ww}}> {2:<{rw}}    file ({3:<{pw}}).\n".format(r[1], r[0], r[2], r[3], lw=l_width, rw=r_width, ww=w_width, pw=p_width))
        self.conc_output_area.configure(state="disabled")
        print("Concordance output for '{}'({} hits) produced in {} seconds.".format(expr, hits, time.time() - t))
    
    def clear_text_area(self):
        self.conc_output_area.configure(state="normal")
        self.conc_output_area.delete(1.0, tk.END)
        self.conc_output_area.configure(state="disabled")

def main():
    openconc = Application()
    openconc.master.title("Open Concordance")
    openconc.mainloop()

if __name__ == "__main__":
    main()
