import tkinter as tk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Frame principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Título
        self.titulo = tk.Label(self.frame, text="Gestión de Nóminas", font=("Arial", 16))
        self.titulo.pack(pady=20)

        # Botones principales
        self.crear_botones()

    def crear_botones(self):
        botones = [
            ("Altas de Empleados", self.abrir_altas),
            ("Bajas de Empleados", self.abrir_bajas),
            ("Informes", self.abrir_informes),
            ("Nóminas", self.abrir_nominas)
        ]

        for texto, comando in botones:
            boton = tk.Button(self.frame, text=texto, width=25, command=comando)
            boton.pack(pady=10)

    def abrir_altas(self):
        from views.altas_view import AltasView
        AltasView(tk.Toplevel(self.root), self.controller)

    def abrir_bajas(self):
        from views.bajas_view import BajasView
        BajasView(tk.Toplevel(self.root), self.controller)

    def abrir_informes(self):
        from views.informes_view import InformesView
        InformesView(tk.Toplevel(self.root), self.controller)

    def abrir_nominas(self):
        from views.nominas_view import NominasView
        NominasView(tk.Toplevel(self.root), self.controller)