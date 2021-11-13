import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('AquaPython App')
        self.resizable(False, False)
        self.create_widgets()

    def caixa_dagua_necessaria(self, volume_necessario):
        dimensoes = [300, 500,1000,1500,2000,3000,5000]
        for d in dimensoes:
            if d > volume_necessario:
                return d

    def consumo_reservatorio(self):
        """
        cp = consumo per capita
        n = numero de pessoas
        dia_suprir = dias a suprir
        """
        cp = float(self.username_entry.get())
        n = int(self.password_entry.get())
        dias_suprir = 1
        volume =  cp*n*dias_suprir*1.2
        caixa = self.caixa_dagua_necessaria(volume)
        messagebox.showinfo("Caixa d'água",f"Consumo diário {volume}L\n Utilizar caixa d'água de {caixa}L")

    def create_widgets(self):
        self.img = ImageTk.PhotoImage(Image.open("caixa_svg.png"))
        #img = tk.PhotoImage("caixadagua.png")
        self.panel = ttk.Label(self, image = self.img)
        self.panel.grid(column=0,row=0, columnspan=2)
        self.username_label = ttk.Label(self, text="Consumo per capita (L/dia):")
        self.username_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # password
        self.password_label = ttk.Label(self, text="Nº de pessoas:")
        self.password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.password_entry = ttk.Entry(self)
        self.password_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # login button
        button = ttk.Button(self, text="Calcular", command=self.consumo_reservatorio)
        button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()