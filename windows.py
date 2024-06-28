import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class MainWindow(tk.Tk):
    def __init__(self,
                height = 1080,
                width = 720):
        super().__init__()
        self.title("TPV")
        self.geometry(f'{height}x{width}')
        self.resultado = 0
        self.resizable(False, False)
        self.ini_bd()

        # self.label = tk.Label(self, text="Producto:")
        # self.label.place(x=0, y=0,)

        # self.entry = tk.Entry(self)
        # self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Nuevo cliente", command=self.new_pax)
        self.button.place(x=10, y=10, width=300)

        # self.button = tk.Button(self, text="Administrar stock", command=self.admin_stock)
        # self.button.place(x=10, y=40, width=300)
        
        self.lb_resultado = tk.Label(self, text=f"{float(self.resultado)}€", font=20, bg="white")
        self.lb_resultado.place(x=width-200, y=height*0.05, width=500)

        self.lb_resultado = tk.Label(self, text=f"{self.usuarios[0]}€", font=20, bg="white")
        self.lb_resultado.place(x=width-200, y=height*0.05, width=500)

        #- - - - - - - - - - - - - 
        # Treeview
        
        
        # self.listbox = tk.Listbox(self)
        # self.listbox.pack(pady=10)

    def add_product(self):
        product = self.entry.get()
        if product:
            self.listbox.insert(tk.END, product)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce un producto.")

    def admin_stock(self):
        self.resultado += 1.0
        self.update_label(self.lb_resultado, self.resultado)

    def new_pax(self):
        self.resultado = 0.0
        self.update_label(self.lb_resultado, self.resultado)

    def update_label(self, label, value):
        label.config(text=f"{value}€")

    def ini_bd(self):
        conn = sqlite3.connect("mi_base_de_datos.db")
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL)
        ''')
        cursor.execute('''
        INSERT INTO usuarios (nombre, precio)
        VALUES ('Alejandro Castro', 99.99)
        ''')
        conn.commit()
        cursor.execute('''
        SELECT * FROM usuarios
        ''')
        self.usuarios = cursor.fetchall()
    