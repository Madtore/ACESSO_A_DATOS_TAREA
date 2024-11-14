from tkinter import *
from tkinter import ttk
from data_base import DataBase
from empleado import Empleado


class Ventana_consulta():

    def __init__(self, ventana_principal):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("1200x600")
        self.ventana.title("Consulta")
        self.ventana.resizable(0, 0)
        self.ventana.grab_set()

        for col in range(6):
            self.ventana.grid_columnconfigure(col, weight=1)

        self.dimensi_caratere = 12

        self.codigo = StringVar()
        self.apellido_nombre = StringVar()
        self.fecha_inicio = StringVar()
        self.fecha_fin = StringVar()
        self.direccion = StringVar()
        self.nif = StringVar()
        self.datos_bancarios = StringVar()
        self.numero_seguro_social = StringVar()
        self.salario_bruto = StringVar()
        self.numero_pagos = StringVar()
        self.salario_mensual = StringVar()
        self.irpf = StringVar()
        self.retencion_irpf = StringVar()
        self.deduccion_irpf = StringVar()
        self.prorrata_pagas = StringVar()
        self.seg_social = StringVar()
        self.deduccion_ss = StringVar()
        self.a_percibir = StringVar()
        self.validacions = StringVar()  

        self.validacions.set("Mensaje de validación")


        for col in range(6): 
            self.ventana.grid_columnconfigure(col, weight=1)



        #linea1
        Label(self.ventana, text="Código", font=("Arial", self.dimensi_caratere)).grid(row=1, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        Label(self.ventana, text="Apellido y Nombre", font=("Arial", self.dimensi_caratere)).grid(row=1, column=2, columnspan=5, pady=10, padx=10, sticky="EW")
        
        Entry(self.ventana, textvariable=self.codigo,justify="center", font=("Arial", self.dimensi_caratere) ).grid(row=2, column=0, columnspan=1, pady=10, padx=10 , sticky="EW")
        Entry(self.ventana, textvariable=self.apellido_nombre, state="readonly" ,justify="center", font=("Arial", self.dimensi_caratere)).grid(row=2, column=2, columnspan=5, pady=10, padx=10, sticky="EW")

        #linea2
        Label(self.ventana, text="Fecha de inicio", font=("Arial", self.dimensi_caratere)).grid(row=4, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        Label(self.ventana, text="Fecha de fin", font=("Arial", self.dimensi_caratere)).grid(row=4, column=1, columnspan=1, pady=10, padx=10, sticky="EW")
        Label(self.ventana, text="Dirección", font=("Arial", self.dimensi_caratere)).grid(row=4, column=2, columnspan=4, pady=10, padx=10, sticky="EW")
        
        Entry(self.ventana, textvariable=self.fecha_inicio,state="readonly",justify="center", font=("Arial", self.dimensi_caratere)).grid(row=5, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        Entry(self.ventana, textvariable=self.fecha_fin ,state="readonly",  justify="center", font=("Arial", self.dimensi_caratere)).grid(row=5, column=1, columnspan=1, pady=10, padx=10, sticky="EW")
        Entry(self.ventana, textvariable=self.direccion , state="readonly", justify="center", font=("Arial", self.dimensi_caratere)).grid(row=5, column=2, columnspan=4, pady=10, padx=10, sticky="EW")
        
        #linea 3
        Label(self.ventana , text="NIF", font=("Arial",self.dimensi_caratere)).grid(row=7, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.nif, state="readonly", justify="center",font=("Arial", self.dimensi_caratere)).grid(row=8, column=0, columnspan=1, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Datos bancarios", font=("Arial", self.dimensi_caratere)).grid(row=7, column=1, columnspan=3, padx=10 )
        Entry(self.ventana , textvariable=self.datos_bancarios, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=8, column=1, columnspan=3, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Numero seguro social", font=("Arial", self.dimensi_caratere)).grid(row=7, column=4, columnspan=2, padx=10 , sticky="EW")
        Entry(self.ventana , textvariable=self.numero_seguro_social, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=8, column=4, columnspan=2, pady=10, padx=10 , sticky="EW")
        
        #linea 4
        Label(self.ventana, text="Salario bruto", font=("Arial", self.dimensi_caratere)).grid(row=9, column=0, columnspan=1, padx=10 )
        Entry(self.ventana, textvariable=self.salario_bruto, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=9, column=1, columnspan=1, pady=10, padx=10 , sticky="EW")
        Label(self.ventana, text="Numero de pagos", font=("Arial", self.dimensi_caratere)).grid(row=9, column=2, columnspan=1, padx=10 )
        Entry(self.ventana, textvariable=self.numero_pagos, justify="center", font=("Arial", self.dimensi_caratere)).grid(row=9, column=3, columnspan=1, pady=10, padx=10 , sticky="EW")

        Label(self.ventana, text="").grid(row=10, column=6, columnspan=6, pady=10, padx=10, sticky="EW")

        ttk.Separator(self.ventana, orient=HORIZONTAL).grid(row=11, columnspan=6, sticky="EW")
        Label(self.ventana, text="").grid(row=11, column=6, columnspan=6, pady=10, padx=10, sticky="EW")


        #linea 5
        Label(self.ventana , text="Salario mensual", font=("Arial", self.dimensi_caratere)).grid(row=12, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.salario_mensual, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=12, column=1, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="IRPF %", font=("Arial", self.dimensi_caratere)).grid(row=12, column=2, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.irpf, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=12, column=3, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="Retencion IRPF", font=("Arial", self.dimensi_caratere)).grid(row=12, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.retencion_irpf, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=12, column=5, columnspan=1, pady=10, padx=10 )

        
        #linea 6
        Label(self.ventana , text="Prorrata pagas", font=("Arial", self.dimensi_caratere)).grid(row=14, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.prorrata_pagas,font=("Arial", self.dimensi_caratere)).grid(row=14, column=1, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="Seg. Social", font=("Arial", self.dimensi_caratere)).grid(row=14, column=2, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.seg_social, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=14, column=3, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="Deduccion SS", font=("Arial", self.dimensi_caratere)).grid(row=14, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.deduccion_ss, justify="center", state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=14, column=5, columnspan=1, pady=10, padx=10 )


        #linea 7
        Entry(self.ventana , textvariable=self.validacions, justify="center" , state="readonly" ,  fg="red", font=("Arial", self.dimensi_caratere)).grid(row=16, column=0, columnspan=3, pady=10, padx=10 , sticky="EW") 
        Label(self.ventana , text="A percibir", font=("Arial", self.dimensi_caratere)).grid(row=16, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.a_percibir, justify="center",  state="readonly",font=("Arial", self.dimensi_caratere)).grid(row=16, column=5, columnspan=1, pady=10, padx=10 )

        Label(self.ventana, text="").grid(row=17, column=0, columnspan=6, pady=10, padx=10, sticky="EW")
        # #linea 8
        Button(self.ventana , text="Cargar empleado", command=self.car_empleado,font=("Arial", self.dimensi_caratere)).grid(row=18, column=0, columnspan=3, pady=10, padx=10 , sticky="EW")
        Button(self.ventana , text="Calcular",command=self.calular, font=("Arial", self.dimensi_caratere)).grid(row=18, column=3, columnspan=2, pady=10, padx=10 , sticky="EW")
        Button(self.ventana , text="Imprimir",command=self.imprimir, font=("Arial", self.dimensi_caratere)).grid(row=18, column=5, columnspan=2, pady=10, padx=10 , sticky="EW")
        
        
        
    def car_empleado(self):
        db = DataBase()
        empleado = db.buscar_empleado(self.codigo.get())
        print(empleado)
        self.apellido_nombre.set(empleado.apellido_nombre)
        self.fecha_inicio.set(empleado.fecha_inicio)
        self.direccion.set(empleado.direccion)
        self.nif.set(empleado.nif)
        self.datos_bancarios.set(empleado.datos_bancarios)
        self.numero_seguro_social.set(empleado.numero_seguro_social)
        self.salario_bruto.set(empleado.salario_mensual*12)
        self.salario_mensual.set(empleado.salario_mensual)
        self.irpf.set(empleado.irpf)
        self.seg_social.set(empleado.seg_social)
        
       
    
    def calular (self):

        salario_anual =float(self.salario_bruto.get())
        salario_mensual = float(self.salario_mensual.get())
        numero_pagos =float(self.numero_pagos.get())  # Número de pagas (12 o 14)
        
        if numero_pagos == 14:
            prorrata_paginas = salario_anual / 14 - salario_mensual
            salario_bruto_mensual = salario_mensual + prorrata_paginas
        else:
            salario_bruto_mensual = salario_mensual
        
        irpf = float(self.irpf.get())
        seg_social = float(self.seg_social.get())

        # Calcular deducciones
        deduccion_irpf = salario_bruto_mensual * (irpf / 100)
        deduccion_seg_social = salario_bruto_mensual * (seg_social / 100)

        # Calcular salario neto a percibir
        salario_neto = salario_bruto_mensual - deduccion_irpf - deduccion_seg_social

        # Actualizar los atributos de salida
        self.deduccion_irpf.set(deduccion_irpf)
        self.deduccion_ss.set(deduccion_seg_social)
        self.a_percibir.set(salario_neto)
        
        
    def imprimir (self):
        print("imprimir")