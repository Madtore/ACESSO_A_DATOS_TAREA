import calendar
from tkinter import *
from tkinter import ttk
from datetime import *

class VentanaFactura:
    def __init__(self, ventana_principal, empleado):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("1400x600")
        self.ventana.title("Factura")
        self.ventana.resizable(0, 0)
        self.ventana.grab_set()

        self.mes = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"}

        text = Text(self.ventana, height=50, width=200)
        text.tag_configure("stile", font=("Arial", 16), spacing1=10, spacing3=10)
        text.insert(END, "Empleado: ", "stile")
        text.insert(END, empleado.apellido_nombre, "stile")
        text.insert(END, "\n", "stile")

        text.insert(END, "Dirección: ", "stile")
        text.insert(END, empleado.direccion, "stile")
        text.insert(END, "\n", "stile")

        text.insert(END, "NIF: ", "stile")
        text.insert(END, empleado.nif, "stile")
        text.insert(END, "\t\t", "stile")

        text.insert(END, "CCC: ", "stile")
        text.insert(END, empleado.datos_bancarios, "stile")
        text.insert(END, "\t\t", "stile")

        text.insert(END, "NAF: ", "stile")
        text.insert(END, empleado.numero_seguro_social, "stile")

        text.insert(END, "\n", "stile")
        text.insert(END, "PERIODO: ", "stile")
        text.insert(END, self.mes[datetime.today().month], "stile")

        text.insert(END, "\t\t", "stile")
        text.insert(END, "DIAS : ", "stile") 
        text.insert(END, str(calendar.monthrange(datetime.today().year, datetime.today().month)[1]), "stile")

        text.insert(END, "\t\t", "stile")
        text.insert(END, "FECHA ALTA: ", "stile")
        text.insert(END, empleado.fecha_inicio, "stile")

        text.insert(END, "\t\t", "stile")
        text.insert(END, "FECHA BAJA: ", "stile")
        print(empleado.fecha_baja)
        if empleado.fecha_baja == None:
            text.insert(END, "", "stile")
        else:
            text.insert(END, empleado.fecha_baja, "stile")

        text.insert(END, "\n", "stile")
        text.insert(END, "SALARIO BASE: ", "stile")
        text.insert(END, "\t\t\t\t\t\t\t\t\t\t\t", "stile")
        text.insert(END, empleado.salario_mensual+" €", "stile")
        text.insert(END, "\n", "stile")

        


        text.pack()

        print(empleado)

        
        