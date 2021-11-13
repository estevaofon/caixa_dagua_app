import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

def caixa_dagua_necessaria(volume_necessario):
    dimensoes = [300, 500,1000,1500,2000,3000,5000]
    for d in dimensoes:
        if d > volume_necessario:
            return d

def consumo_reservatorio():
    """
    cp = consumo per capita
    n = numero de pessoas
    dia_suprir = dias a suprir
    """
    cp = float(username_entry.get())
    n = int(password_entry.get())
    dias_suprir = 1
    volume =  cp*n*dias_suprir*1.2
    caixa = caixa_dagua_necessaria(volume)
    messagebox.showinfo("Caixa d'água",f"Consumo diário {volume}L\n Utilizar caixa d'água de {caixa}L")


root = tk.Tk()
img = ImageTk.PhotoImage(Image.open("caixadagua_branca.png"))
#img = tk.PhotoImage("caixadagua.png")
panel = ttk.Label(root, image = img)
panel.grid(column=0,row=0, columnspan=2)
username_label = ttk.Label(root, text="Consumo per capita (L/dia):")
username_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Nº de pessoas:")
password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# login button
button = ttk.Button(root, text="Calcular", command=consumo_reservatorio)
button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()