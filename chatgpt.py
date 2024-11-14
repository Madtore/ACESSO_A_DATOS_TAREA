import tkinter as tk
from tkinter import messagebox

class AltasWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Altas de Empleados")
        self.geometry("500x600")
        
        # Título principal
        tk.Label(self, text="Registro de Empleado", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Campos de entrada
        labels = [
            "Apellidos y Nombre", "Fecha de Inicio", "Fecha de Nacimiento", "Dirección",
            "NIF", "Datos Bancarios", "Número de Afiliación SS", "Departamento",
            "Género", "Puesto", "Teléfono", "Salario Mensual", "Pagas Extra",
            "IRPF (%)", "Seguridad Social", "Email"
        ]
        
        # Crear campos y etiquetas en una cuadrícula
        self.entries = {}
        for idx, text in enumerate(labels):
            # Etiquetas de los campos
            tk.Label(self, text=text).grid(row=idx+1, column=0, sticky="w", padx=10, pady=5)
            # Campos de entrada
            entry = tk.Entry(self, width=30)
            entry.grid(row=idx+1, column=1, padx=10, pady=5)
            # Guardamos cada campo en un diccionario para uso futuro si es necesario
            self.entries[text] = entry

        # Botón de Inserción
        tk.Button(self, text="Insertar", command=self.insert_employee, bg="lightblue").grid(row=len(labels)+1, column=1, pady=20)

    def insert_employee(self):
        # Mensaje de confirmación para simular la inserción del empleado
        messagebox.showinfo("Insertar Empleado", "Empleado insertado correctamente.")

# Ejecuta la ventana de "Altas" directamente
if __name__ == "__main__":
    app = AltasWindow()
    app.mainloop()

