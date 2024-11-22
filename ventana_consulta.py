from tkinter import *
from tkinter import ttk
from data_base import DataBase
from empleado import Empleado
from ventana_nomina import VentanaNomina


class Ventana_consulta():

    def __init__(self, ventana_principal):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("1400x600")
        self.ventana.title("Consulta")
        self.ventana.grab_set()

        for col in range(6):
            self.ventana.grid_columnconfigure(col, weight=1)

        self.empleado = Empleado()

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

        stile = {"font":("Arial", 14)}

        #linea1
        Label(self.ventana, text="Código",**stile).grid(row=1, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        Label(self.ventana, text="Apellido y Nombre", **stile).grid(row=1, column=2, columnspan=5, pady=10, padx=10, sticky="EW")
        
        Entry(self.ventana, textvariable=self.codigo,justify="center", **stile ).grid(row=2, column=0, columnspan=1, pady=10, padx=10 , sticky="EW")
        Entry(self.ventana, textvariable=self.apellido_nombre, state="readonly" ,justify="center", **stile).grid(row=2, column=2, columnspan=5, pady=10, padx=10, sticky="EW")

        #linea2
        Label(self.ventana, text="Fecha de inicio", **stile).grid(row=4, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        Label(self.ventana, text="Fecha de fin", **stile).grid(row=4, column=1, columnspan=1, pady=10, padx=10, sticky="EW")
        Label(self.ventana, text="Dirección", **stile).grid(row=4, column=2, columnspan=4, pady=10, padx=10, sticky="EW")
        
        Entry(self.ventana, textvariable=self.fecha_inicio,state="readonly",justify="center", **stile).grid(row=5, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        Entry(self.ventana, textvariable=self.fecha_fin ,state="readonly",  justify="center", **stile).grid(row=5, column=1, columnspan=1, pady=10, padx=10, sticky="EW")
        Entry(self.ventana, textvariable=self.direccion , state="readonly", justify="center", **stile).grid(row=5, column=2, columnspan=4, pady=10, padx=10, sticky="EW")
        
        #linea 3
        Label(self.ventana , text="NIF", **stile).grid(row=7, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.nif, state="readonly", justify="center", **stile).grid(row=8, column=0, columnspan=1, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Datos bancarios", **stile).grid(row=7, column=1, columnspan=3, padx=10 )
        Entry(self.ventana , textvariable=self.datos_bancarios, justify="center", state="readonly", **stile).grid(row=8, column=1, columnspan=3, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Numero seguro social", **stile).grid(row=7, column=4, columnspan=2, padx=10 , sticky="EW")
        Entry(self.ventana , textvariable=self.numero_seguro_social, justify="center", state="readonly", **stile).grid(row=8, column=4, columnspan=2, pady=10, padx=10 , sticky="EW")
        
        #linea 4
        Label(self.ventana, text="Salario bruto", **stile).grid(row=9, column=0, columnspan=1, padx=10 )
        Entry(self.ventana, textvariable=self.salario_bruto, justify="center", state="readonly",**stile).grid(row=9, column=1, columnspan=1, pady=10, padx=10 , sticky="EW")
        Label(self.ventana, text="Numero de pagos", **stile).grid(row=9, column=2, columnspan=1, padx=10 )
        Entry(self.ventana, textvariable=self.numero_pagos, justify="center", state="readonly", **stile).grid(row=9, column=3, columnspan=1, pady=10, padx=10 , sticky="EW")

        Label(self.ventana, text="").grid(row=10, column=6, columnspan=6, pady=10, padx=10, sticky="EW")

        ttk.Separator(self.ventana, orient=HORIZONTAL).grid(row=11, columnspan=6, sticky="EW")
        Label(self.ventana, text="").grid(row=11, column=6, columnspan=6, pady=10, padx=10, sticky="EW")


        #linea 5
        Label(self.ventana , text="Salario mensual", **stile).grid(row=12, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.salario_mensual, justify="center", state="readonly", **stile).grid(row=12, column=1, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="IRPF %", **stile).grid(row=12, column=2, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.irpf, justify="center", state="readonly", **stile).grid(row=12, column=3, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="Retencion IRPF", **stile).grid(row=12, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.retencion_irpf, justify="center", state="readonly", **stile).grid(row=12, column=5, columnspan=1, pady=10, padx=10 )

        
        #linea 6
        Label(self.ventana , text="Prorrata pagas",  **stile).grid(row=14, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.prorrata_pagas,justify="center", state="readonly", **stile).grid(row=14, column=1, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="Seg. Social",  **stile).grid(row=14, column=2, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.seg_social, justify="center", state="readonly", **stile).grid(row=14, column=3, columnspan=1, pady=10, padx=10 )
        
        Label(self.ventana , text="Deduccion SS",  **stile).grid(row=14, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.deduccion_ss, justify="center", state="readonly", **stile).grid(row=14, column=5, columnspan=1, pady=10, padx=10 )


        #linea 7
        Entry(self.ventana , textvariable=self.validacions, justify="center" , state="readonly" ,  fg="red", **stile).grid(row=16, column=0, columnspan=3, pady=10, padx=10 , sticky="EW") 
        Label(self.ventana , text="A percibir", **stile).grid(row=16, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.a_percibir, justify="center",  state="readonly", **stile).grid(row=16, column=5, columnspan=1, pady=10, padx=10 )

        #Label(self.ventana, text="").grid(row=17, column=0, columnspan=6, pady=10, padx=10, sticky="EW")
        # #linea 8
        Button(self.ventana , text="Cargar empleado" ,  background="#2ECC71", command=self.car_empleado,**stile).grid(row=18, column=0, columnspan=3, pady=10, padx=10 , sticky="EW")
        Button(self.ventana , text="Calcular", background="#4169e1",command=self.carcular, **stile).grid(row=18, column=3, columnspan=2, pady=10, padx=10 , sticky="EW")
        Button(self.ventana , text="Imprimir", background="#4169e1",command=self.imprimir, **stile).grid(row=18, column=5, columnspan=2, pady=10, padx=10 , sticky="EW")
        
        
        
    def car_empleado(self):
        self.validacions.set("")
        self.a_percibir.set("")
        self.retencion_irpf.set("")
        self.deduccion_irpf.set("")
        self.deduccion_ss.set("")
        self.prorrata_pagas.set("")
        self.seg_social.set("")

        db = DataBase()
        try:
            empleado = db.buscar_empleado(self.codigo.get())
            self.apellido_nombre.set(empleado.apellido_nombre)
            self.fecha_inicio.set(empleado.fecha_inicio)
            print(empleado.fecha_baja)
            if empleado.fecha_baja == None:
                self.fecha_fin.set("")
            else:
                self.fecha_fin.set(empleado.fecha_baja)
            
            self.direccion.set(empleado.direccion)
            self.nif.set(empleado.nif)
            self.datos_bancarios.set(empleado.datos_bancarios)
            self.numero_seguro_social.set(empleado.numero_seguro_social)
            self.salario_bruto.set(empleado.salario_mensual*(12+empleado.paga_extra))
            print(empleado.salario_mensual*(12+empleado.paga_extra))
            self.salario_mensual.set(empleado.salario_mensual)
            self.numero_pagos.set(empleado.paga_extra+12)
            self.irpf.set(empleado.irpf)
            self.seg_social.set(empleado.seg_social)
            self.empleado = empleado
        except:
            self.validacions.set("Empleado con codigo {} no encontrado".format(self.codigo.get()))
            return
        
        print(empleado)
        
        
       
    
    def carcular (self):

        salario_mensual = float(self.salario_mensual.get())
        numero_pagos =float(self.numero_pagos.get())  
        
        if numero_pagos > 12:
            paga_extra = salario_mensual 
            numero_pagas_extra = numero_pagos - 12
            prorrata_pagas = round((paga_extra * numero_pagas_extra) / 12, 2)
            salario_bruto_mensual = salario_mensual + prorrata_pagas
        else:
            salario_bruto_mensual = salario_mensual
            prorrata_pagas = 0
        
        irpf = float(self.irpf.get())
        seg_social = float(self.seg_social.get())

        deduccion_irpf = round(salario_bruto_mensual * (irpf / 100), 2)
        deduccion_seg_social = round(salario_bruto_mensual * (seg_social / 100), 2)

        salario_neto = round(salario_bruto_mensual - deduccion_irpf - deduccion_seg_social, 2)
        
        
        self.prorrata_pagas.set(prorrata_pagas) 
        self.retencion_irpf.set(deduccion_irpf)
        self.deduccion_ss.set(deduccion_seg_social)
        self.a_percibir.set(salario_neto)
        
        
    def imprimir (self):
        self.datos = {
            'prorrata_pagas': self.prorrata_pagas.get(),
            'retencion_irpf': self.retencion_irpf.get(),
            'deduccion_ss': self.deduccion_ss.get(),
            'a_percibir': self.a_percibir.get(),
        }
        VentanaNomina(self.ventana, self.empleado , self.datos) 
        
        
        

         