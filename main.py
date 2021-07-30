# Librerie
import tkinter as tk
import sys
import random
import os
from tkinter import *
from tkinter import filedialog
from termcolor import colored
# Funzioni database
import asin
import cleaning
import merge
import add_category
import add_aggiornamento
import drop
import delete
import dbsettings
import help
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, bg='#2d3436', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg='#2d3436', highlightthickness=0)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class MenuBar:

    def __init__(self, parent):
        font = ('Corbel', 14)
        font_2 = ('Corbel', 10)

        menubar = tk.Menu(parent.root, font=font)
        parent.root.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_2, tearoff=0)

        file_dropdown.add_command(label="Impostazioni connessione",
                                  command=parent.connection_setting)
        file_dropdown.add_command(label="Help", command=parent.help)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Esci", command=parent.root.destroy)

        menubar.add_cascade(label="Opzioni", menu=file_dropdown)

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget

        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible
        self.textbox.config(state=tk.DISABLED)

        self.textbox.insert(END, "spam\n")
        self.textbox.see(END)

    def flush(self): # needed for file like object
        pass


class Main:
    def __init__(self, root):
        self.colors = ["#c8d6e5", "#636e72", "#c0392b", "#ff3838", "#2d3436", "#d1d8e0", "#2d3436", "#2980b9", "#2980b9"]
        root.geometry("500x620")
        root.title('DB manager')
        root.resizable(0, 0)
        root.grid_columnconfigure(0, weight=1)
        root.configure(background=self.colors[4])
        root.iconbitmap(r'img/icon.ico')

        self.root = root
        # frame = ScrollableFrame(root)

        self.frame_1 = tk.Frame(root, bg='#2d3436', width=100)
        self.frame = ScrollableFrame(self.frame_1)

        font_1 = ("Bebas", 32, 'bold')
        font_2 = ("Consolas", 12)
        font_3 = ("Bahnschrift", 10)

        self.title = tk.Label(root, text="DATABASE",
                              font=font_1, fg=self.colors[3],bg=self.colors[1], relief="raised")
        self.title.grid(pady=15, padx=100,sticky="we")

        self.frame_1.grid(sticky="")

        asin_btn = tk.Button(
            self.frame.scrollable_frame,
            text='Estrapola asin',
            command=self.get_asin,
            font=font_3,
            bg=self.colors[0],
            border=0.5,
            width=50
        )
        asin_btn.grid(pady=5, sticky="ew", ipady=5, padx=10)

        clean_btn = tk.Button(self.frame.scrollable_frame, text='Elabora amazon_it', command=self.cleaning, font=font_3, bg=self.colors[0], border=0.5)
        clean_btn.grid(pady=5, sticky="ew", ipady=5, padx=10)

        merge_btn = tk.Button(self.frame.scrollable_frame, text='Tabella unica', command=self.merge, font=font_3, bg=self.colors[0], border=0.5)
        merge_btn.grid(pady=5, sticky="ew", ipady=5, padx=10)

        add_category = tk.Button(self.frame.scrollable_frame, text='Aggiungi Categoria', command=self.add_category, font=font_3, bg=self.colors[0], border=0.5)
        add_category.grid(pady=5, sticky="ew", ipady=5, padx=10)

        add_agg = tk.Button(self.frame.scrollable_frame, text='Aggiungi Aggiornamento', command=self.add_agg, font=font_3, bg=self.colors[0], border=0.5)
        add_agg.grid(pady=5, sticky="ew", ipady=5, padx=10)

        drop = tk.Button(self.frame.scrollable_frame, text='Elimina tabella', command=self.drop, font=font_3, bg=self.colors[0], border=0.5)
        drop.grid(pady=5, sticky="ew", ipady=5, padx=10)

        delete = tk.Button(self.frame.scrollable_frame, text='Elimina dati tabella', command=self.delete, font=font_3, bg=self.colors[0], border=0.5)
        delete.grid(pady=5, sticky="ew", ipady=5, padx=10)


        self.t = tk.Text(root, state=tk.DISABLED, bg=self.colors[5], fg="black", height=8,font = font_2,
                         border=3 ,selectbackground=self.colors[6])
        self.t.grid(pady=2, padx=3, sticky="we")

        self.clear_console = tk.Button(root, text='Pulisci console', bg="#c0392b", command=self.clear_console, border=0.5)
        self.clear_console.grid(sticky="ew", padx=4)

        self.frame.grid(sticky="W")

        self.menubar = MenuBar(self)

        pl = PrintLogger(self.t)
        sys.stdout = pl
        print("DATABASE MANAGER...")
        self.t.insert(END, "spam\n")
        self.t.see(END)


        # root.after(10, self.do_something)

    def get_asin(self): # Funzione per prendere gli asin da una determinata tabella in un determinato db
        mask = [
            ("Text files", "*.txt"),
            ("All files", "*.*")]

        file_name = filedialog.asksaveasfilename(title="Salva File ASIN", filetype=mask)
        print("Percorso file asin:",file_name)
        with open("cache/file_path.txt", "w+") as f:
            f.write(file_name)

        dbsettings.Run()
        print("Estrapolazione asin in corso...")
        asin.Asin()

    def cleaning(self):
        print("Creazione tabella disponibili_no_doppioni...")
        dbsettings.Run_2()
        cleaning.Clean()

    def merge(self):
        print("Creazione tabella_unica...")
        merge.Merge()

    def add_category(self):
        print("Aggiunta Categoria in tabella_unica...")
        add_category.Add_category()

    def add_agg(self):
        print("Aggiunto Aggiornamento int tabella_unica...")
        add_aggiornamento.Add_agg()

    def delete(self):
        print("Eliminazione dati tabella...")
        dbsettings.Run()
        delete.Delete()

    def drop(self):
        print("Eliminazione Tabella...")
        dbsettings.Run()
        drop.Drop()

    def do_something(self):
        print('i did something')
        root.after(10, self.do_something)

    def clear_console(self):
        colors = ["#27ae60", "#c0392b"]
        self.t.config(state=tk.NORMAL)
        self.t.delete('1.0', tk.END)
        self.t.config(state=tk.DISABLED)

        if self.t:
            self.clear_console.configure(bg=colors[0])
        else:
            self.clear_console.configure(bg=colors[1])


    def connection_setting(self):
        os.system("cd cache & connection.txt")

    def help(self):
        help.Run()



if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    root.mainloop()