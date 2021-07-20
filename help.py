import tkinter as tk
from tkinter import messagebox
from tkinter import *

class Help:
    def __init__(self, root):
        self.colors = ["#c8d6e5", "#636e72", "#c0392b", "#ff3838", "#2d3436", "#d1d8e0", "#2d3436", "#2980b9",
                       "#2980b9"]
        root.geometry("500x500")
        root.title('DB manager - Help')
        root.resizable(1, 1)
        root.configure(background='#e6f2ff')
        root.iconbitmap(r'img/icon.ico')
        font = ("ubuntu", 14)
        font_2 = ("Consolas", 14)

        self.root = root

        self.t = tk.Text(root, state=tk.DISABLED, bg=self.colors[5], fg="black", height=8, font=font_2,
                         border=3, selectbackground=self.colors[6])
        self.scroll = tk.Scrollbar(root, command=self.t.yview)
        self.t.configure(yscrollcommand=self.scroll.set)
        self.t.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.write()


    def write(self):
        self.t.configure(state=tk.NORMAL)
        with open("cache/help.txt", "r") as f:
            self.t.insert(1.0, f.read())
        self.t.configure(state=tk.DISABLED)


class Run:
    def __init__(self):
        # print("qui")
        root = tk.Toplevel()
        main = Help(root)
        root.mainloop()