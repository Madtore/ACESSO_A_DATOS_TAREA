import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AltasView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Alta de Empleados")
        self.root.geometry("600x800")

        self.crear_formulario()

    def crear_formulario(self):
        # Crear un Frame contenedor
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

        # Campos del formulario
        campos = [
            ("Código", "codigo"),
            ("Apellidos", "apellidos"),
            ("Nombre", "nombre"),
            ("NIF", "nif"),
            ("Dirección", "direccion"),
            ("Teléfono", "telefono"),
            ("Email", "email"),
            ("Número Afiliación SS", "numero_ss"),
            ("Departamento", "departamento"),
            ("Puesto", "puesto")
        ]

        # Variables para los campos
        self.variables = {}
        for i, (etiqueta, nombre) in enumerate(campos):
            lbl = tk.Label(frame, text=etiqueta)
            lbl.grid(row=i, column=0, sticky="w", padx=5, pady=5)
            
            entrada = tk.Entry(frame, width=40)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            
            self.variables[nombre] = entrada

        # Campos de fecha
        lbl_fecha_nacimiento = tk.Label(frame, text="Fecha Nacimiento")
        lbl_fecha_nacimiento.grid(row=len(campos), column=0, sticky="w", padx=5, pady=5)
        self.fecha_nacimiento = DateEntry(frame, width=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_nacimiento.grid(row=len(campos), column=1, padx=5, pady=5)

        lbl_fecha_inicio = tk.Label(frame, text="Fecha Inicio")
        lbl_fecha_inicio.grid(row=len(campos)+1, column=0, sticky="w", padx=5, pady=5)
        self.fecha_inicio = DateEntry(frame, width=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_inicio.grid(row=len(campos)+1, column=1, padx=5, pady=5)

        # Género
        lbl_genero = tk.Label(frame, text="Género")
        lbl_genero.grid(row=len(campos)+2, column=0, sticky="w", padx=5, pady=5)
        self.genero = ttk.Combobox(frame, values=["Masculino", "Femenino", "Otro"])
        self.genero.grid(row=len(campos)+2, column=1, padx=5, pady=5)

        # Botón de inserción
        btn_insertar = tk.Button(frame, text="Insertar", command=self.insertar_empleado)
        btn_insertar.grid(row=len(campos)+3, column=0, columnspan=2, pady=10)

    def insertar_empleado(self):
        # Recoger datos
        datos = {nombre: entrada.get() for nombre, entrada in self.variables.items()}
        datos['fecha_nacimiento'] = self.fecha_nacimiento.get_date()
        datos['fecha_inicio'] = self.fecha_inicio.get_date()
        datos['genero'] = self.genero.get()

        # Validar y procesar
        try:
            self.controller.insertar_empleado(datos)
            messagebox.showinfo("Éxito", "Empleado insertado correctamente")
            self.root.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))