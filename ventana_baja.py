from tkinter import *
from data_base import *
from empleado import *

class Ventana_baja():
    def __init__(self, ventana_principal  ):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("600x300")
        self.ventana.title("Bajas")
        self.ventana.resizable(0, 0)
        self.ventana.grab_set()

        self.codigo = StringVar()
        self.fecha_baja = StringVar()
        self.validacions = StringVar()
        self.validacions.set("Mensaje de validación") 

       
        for col in range(12): 
            self.ventana.grid_columnconfigure(col, weight=1)

        
        Label(self.ventana, text="Código empleado", font=("Arial", 15)).grid(row=2, column=1, columnspan=4, pady=10, padx=10, sticky="EW")
        self.Entry_codigo = Entry(self.ventana, textvariable=self.codigo)
        self.Entry_codigo.grid(row=3, column=1, columnspan=4, pady=10, sticky="EW")
        
        Label(self.ventana, text="Fecha de baja", font=("Arial", 15)).grid(row=2, column=7, columnspan=4, pady=10, padx=10, sticky="EW")
        self.Entry_fecha_baja = Entry(self.ventana, textvariable=self.fecha_baja)
        self.Entry_fecha_baja.grid(row=3, column=7, columnspan=4, pady=10, sticky="EW")

       
        Label(self.ventana, text="", font=("Arial", 15)).grid(row=4, column=0, pady=10, padx=10)

       
        self.Entr_validar = Entry(self.ventana, textvariable=self.validacions, justify="center",state="readonly", fg="red", font=("Arial", 15))
        self.Entr_validar.grid(row=9, column=1, columnspan=10, rowspan=3, pady=10, sticky="EW") 

       
        self.Button_ventana = Button(self.ventana, text="Confirmar", command=self.confirmar)
        self.Button_ventana.grid(row=15, column=2, columnspan=8, rowspan=2, pady=10, sticky="EW")  
        
        self.ventana.mainloop()
            
    def confirmar(self):
        codigo = self.Entry_codigo.get()
        fecha_baja = self.Entry_fecha_baja.get()
        
        if fecha_baja == "" or codigo == "":
            if codigo != "":
                self.validacions.set("El codigo no puede estar vacio")
                return
            
            if fecha_baja != "":
                self.validacions.set("La fecha de baja no puede estar vacia")
                return
            
            self.validacions.set("La fecha de baja y el codigo no pueden estar vacios")
            return
        
        db = DataBase()
        
        
        if db.buscar_empleado(codigo) == None:
            self.validacions.set("El empleado no existe")
            return
        
        Empleado.darbaja(codigo,fecha_baja)
        
        self.validacions.set("El empleado cod:{} ha sido dado de baja en fecha: {}".format(codigo,fecha_baja))
        return