import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Settings:
    def __init__(self, root):
        root.geometry("400x200")
        root.title('DB manager')
        root.resizable(0, 0)
        root.grid_columnconfigure(0, weight=1)
        root.configure(background='#e6f2ff')
        root.iconbitmap(r'img/icon.ico')
        font = ("ubuntu", 14)

        self.root = root

        self.photo = PhotoImage(file="img/save.png")

        self.title = tk.Label(root, text="Database name", font=font,fg='#c50000', bg="#e6f2ff")
        self.title.grid(pady=15)
        
        self.var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.var, width=60,justify=tk.CENTER, bd=3)
        self.entry.grid()

        self.title2 = tk.Label(root, text="Table name", font=font,fg='#c50000', bg="#e6f2ff")
        self.title2.grid(pady=15)

        self.var2 = tk.StringVar()
        self.entry2 = tk.Entry(root, textvariable=self.var2, width=60,justify=tk.CENTER, bd=3)
        self.entry2.grid()
        
        self.save_btn = tk.Button(root, text="ciao", image=self.photo, border=0, bg="#e6f2ff", command=self.save)
        self.save_btn.grid(sticky="e", padx=7, pady=5)

    def save(self):
        try:
            with open("cache/db_name.txt", "w+") as f:
                f.write(self.entry.get())

            with open("cache/table_name.txt", "w+") as f:
                f.write(self.entry2.get())
        except Exception as e:
            print("Errore:", e)

        with open("cache/db_name.txt", "r") as f:
            a = f.read()

        with open("cache/table_name.txt", "r") as f:
            b = f.read()

        if b == self.entry2.get() and a == self.entry.get():
            messagebox.showinfo("Salvataggio", "Salvataggio eseguito con successo")
            self.root.destroy()
            self.root.quit()
        else:
            raise ("An error occurred")


class Run:
    def __init__(self):
        # print("qui")
        root = tk.Toplevel()
        main = Settings(root)
        root.mainloop()


class Settings_2:
    def __init__(self, root):
        root.geometry("400x200")
        root.title('DB manager')
        root.resizable(0, 0)
        root.grid_columnconfigure(0, weight=1)
        root.configure(background='#e6f2ff')
        root.iconbitmap(r'img/icon.ico')
        font = ("ubuntu", 14)

        self.root = root

        self.photo = PhotoImage(file="img/save.png")

        self.title = tk.Label(root, text="Category Name", font=font, fg='#c50000', bg="#e6f2ff")
        self.title.grid(pady=15)

        self.var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.var, width=60, justify=tk.CENTER, bd=3)
        self.entry.grid()

        self.save_btn = tk.Button(root, text="ciao", image=self.photo, border=0, bg="#e6f2ff", command=self.save)
        self.save_btn.grid(sticky="e", padx=7, pady=5)


    def save(self):
        try:
            with open("cache/category.txt", "w+") as f:
                f.write(self.entry.get())
        except Exception as e:
            print("Errore:", e)

        with open("cache/category.txt", "r") as f:
            a = f.read()


        if a == self.entry.get():
            messagebox.showinfo("Salvataggio", "Salvataggio eseguito con successo")
            self.root.destroy()
            self.root.quit()
        else:
            raise ("An error occurred")




class Run_2:
    def __init__(self):
        # print("qui")
        root = tk.Toplevel()
        main = Settings_2(root)
        root.mainloop()