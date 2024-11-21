import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk  # Requiere: pip install ttkbootstrap

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Nóminas")
        self.root.geometry("600x500")
        
        # Configurar estilo
        style = ttk.Style(theme='solar')
        
        # Crear frame principal
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Título
        self.titulo = ttk.Label(
            self.main_frame, 
            text="Sistema de Gestión de Nóminas", 
            font=('Helvetica', 18, 'bold'),
            bootstyle='primary'
        )
        self.titulo.pack(pady=(0, 30))
        
        # Crear botones con estilo
        botones = [
            ("Altas de Empleados", self.altas_empleados, 'success'),
            ("Bajas de Empleados", self.bajas_empleados, 'danger'),
            ("Informes", self.generar_informes, 'info'),
            ("Gestión de Nóminas", self.gestionar_nominas, 'warning')
        ]
        
        for texto, comando, estilo in botones:
            boton = ttk.Button(
                self.main_frame, 
                text=texto, 
                command=comando,
                bootstyle=f'{estilo}-outline',
                width=30
            )
            boton.pack(pady=10)
        
        # Pie de página
        self.pie = ttk.Label(
            self.main_frame, 
            text="© 2024 Aplicación de Gestión de Nóminas", 
            font=('Helvetica', 10),
            bootstyle='secondary'
        )
        self.pie.pack(side=tk.BOTTOM, pady=20)

    def altas_empleados(self):
        print("Abrir ventana de Altas de Empleados")

    def bajas_empleados(self):
        print("Abrir ventana de Bajas de Empleados")

    def generar_informes(self):
        print("Abrir ventana de Informes")

    def gestionar_nominas(self):
        print("Abrir ventana de Gestión de Nóminas")

def main():
    root = ttk.Window()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()