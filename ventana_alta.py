from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from validador import Validador
from data_base import *
from empleado import *
from tkinter import messagebox



class Ventana_alta():
    def __init__(self, ventana_principal ):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("1400x600")
        self.ventana.title("Altas")
        self.ventana.resizable(0, 0)
        self.ventana.grab_set()

        for col in range(6): 
            self.ventana.grid_columnconfigure(col, weight=1)
            
        self.dimensi_caratere = 14    
            
        self.apellido_nombre = StringVar()
        self.fecha_inicio = StringVar()
        self.fecha_nacimiento = StringVar()
        self.direccion = StringVar()
        self.nif = StringVar()
        self.datos_bancarios = StringVar()
        self.numero_seguro_social = StringVar()    
        self.genero = StringVar()
        self.departamento = StringVar()
        self.puesto = StringVar() 
        self.telefono = StringVar()
        self.salario_mensual = StringVar()
        self.irpf = StringVar()
        self.email = StringVar()
        self.paga_extra = StringVar()
        self.seg_social = StringVar()
        self.validacions = StringVar()
        
        
        self.validacions.set("Mensaje de validación")
        
        stile = {"font": ("Arial", self.dimensi_caratere)}
        
        
        
        #linea 1    
        Label(self.ventana , text="Apellido y Nombre", **stile).grid(row=0, column=0, columnspan=6, padx=10 )
        Entry(self.ventana , textvariable=self.apellido_nombre, **stile).grid(row=1, column=0, columnspan=6, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="").grid(row=2, column=6, columnspan=6, padx=10 , sticky="EW")
        
        #linea 2
        Label(self.ventana , text="Fecha de inicio", **stile).grid(row=3, column=0, columnspan=1, padx=10 )
        DateEntry(self.ventana, textvariable=self.fecha_inicio, **stile, date_pattern="yyyy-mm-dd").grid(row=4, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        
        Label(self.ventana , text="Fecha de nacimiento", **stile).grid(row=3, column=1, columnspan=1, padx=10 )
        DateEntry(self.ventana, textvariable=self.fecha_nacimiento, **stile, date_pattern="yyyy-mm-dd").grid(row=4, column=1, columnspan=1, pady=10, padx=10, sticky="EW")
        
        Label(self.ventana , text="Direccion", **stile).grid(row=3, column=2, columnspan=4, padx=10 , sticky="EW")
        Entry(self.ventana , textvariable=self.direccion, **stile).grid(row=4, column=2, columnspan=4, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="").grid(row=5, column=6, columnspan=6, padx=10 , sticky="EW")
        
        #linea 3
        Label(self.ventana , text="NIF", **stile).grid(row=6, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.nif, **stile).grid(row=7, column=0, columnspan=1, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Datos bancarios", **stile).grid(row=6, column=1, columnspan=3, padx=10 )
        Entry(self.ventana , textvariable=self.datos_bancarios, **stile).grid(row=7, column=1, columnspan=3, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Numero seguro social", **stile).grid(row=6, column=4, columnspan=2, padx=10 , sticky="EW")
        Entry(self.ventana , textvariable=self.numero_seguro_social, **stile).grid(row=7, column=4, columnspan=2, pady=10, padx=10 , sticky="EW")
        
       
        Label(self.ventana , text="").grid(row=8, column=6, columnspan=6, padx=10 , sticky="EW")
       
        #linea 4
        Label(self.ventana , text="Genero", **stile).grid(row=9, column=0, columnspan=1, padx=10 )
        Combobox(self.ventana, textvariable=self.genero, state="readonly", value=("Mujer", "Hombre"), **stile).grid(row=10, column=0, columnspan=1, pady=10, padx=10, sticky="EW")
        
        
        #Entry(self.ventana , textvariable=self.genero, font=("Arial", self.dimensi_caratere)).grid(row=10, column=0, columnspan=1, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Departamento", **stile).grid(row=9, column=1, columnspan=3, padx=10 )
        Entry(self.ventana , textvariable=self.departamento, **stile).grid(row=10, column=1, columnspan=3, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="Puesto", **stile).grid(row=9, column=4, columnspan=2, padx=10 )
        Entry(self.ventana , textvariable=self.puesto, **stile).grid(row=10, column=4, columnspan=2, pady=10, padx=10 , sticky="EW")
        
        Label(self.ventana , text="").grid(row=11, column=6, columnspan=6, padx=10 , sticky="EW")
        
        #linea 5
        Label(self.ventana , text="Telefono", **stile).grid(row=12, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.telefono, **stile).grid(row=12, column=1, columnspan=1, pady=10, padx=10)
        
        Label(self.ventana , text="Salario M.", **stile).grid(row=12, column=2, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.salario_mensual, **stile).grid(row=12, column=3, columnspan=1, pady=10, padx=10)
        
        Label(self.ventana , text="IRPF", **stile).grid(row=12, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.irpf, **stile).grid(row=12, column=5, columnspan=1, pady=10, padx=10)
        
        #linea 6
        Label(self.ventana , text="Email", **stile).grid(row=13, column=0, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.email, **stile).grid(row=13, column=1, columnspan=1, pady=10, padx=10)
        
        Label(self.ventana , text="Paga extra", **stile).grid(row=13, column=2, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.paga_extra, **stile).grid(row=13, column=3, columnspan=1, pady=10, padx=10)
        
        Label(self.ventana , text="SEG. SOCIAL", **stile).grid(row=13, column=4, columnspan=1, padx=10 )
        Entry(self.ventana , textvariable=self.seg_social, **stile).grid(row=13, column=5, columnspan=1, pady=10, padx=10)
        
        Label(self.ventana , text="").grid(row=12, column=6, columnspan=6, padx=10 , sticky="EW")
        Label(self.ventana , text="").grid(row=13, column=6, columnspan=6, padx=10 , sticky="EW")
        Label(self.ventana , text="").grid(row=14, column=6, columnspan=6, padx=10 , sticky="EW")
       
        #linea 7
        Entry(self.ventana, textvariable=self.validacions, justify="center",state="readonly", fg="red", **stile).grid(row=16, column=0, columnspan=4, rowspan=3, pady=10 , padx=10, sticky="EWSN" ) 

        
        Button(self.ventana,  text="Insertar", command=self.confirmar , **stile , background="#7F8C8D").grid(row = 16 , column= 4, columnspan=2, rowspan=3, pady=10 , padx=10, sticky="EWSN" ) 
       
        
        
        
        
    def confirmar(self):
       if self.validarCampos():
            emp = Empleado(
            apellido_nombre=self.apellido_nombre.get(),                
            salario_mensual=self.salario_mensual.get(),                     
            telefono=self.telefono.get(),                          
            email=self.email.get(),                
            fecha_inicio= self.fecha_inicio.get(),                         
            fecha_nacimiento= self.fecha_nacimiento.get(),               
            direccion=self.direccion.get(),           
            nif= self.nif.get(),                               
            datos_bancarios= self.datos_bancarios.get(),   
            numero_seguro_social= self.numero_seguro_social.get(),            
            genero= self.genero.get(),                                    
            departamento= self.departamento.get(),                            
            puesto= self.puesto.get(),                      
            paga_extra= self.paga_extra.get(),
            irpf= self.irpf.get(),
            seg_social= self.seg_social.get(),
                      
            )
            
            print(emp)
            db = DataBase()
            db.insertar(emp)

       
       
            
        
    def validarCampos(self):
        validador = Validador()
        errores = []

        if not validador.validadorGeneral(self.apellido_nombre.get()):
            errores.append("Apellido y Nombre")

        if not validador.validadorFecha(self.fecha_nacimiento.get()):
            errores.append("Fecha de Nacimiento")
            
        if not validador.validadorFecha(self.fecha_inicio.get()):
            errores.append("Fecha de Inicio")

        if not validador.validadorGeneral(self.direccion.get()):
            errores.append("Dirección")

        if not validador.validar_nif(self.nif.get()):
            errores.append("NIF")

        if not validador.validar_ccc(self.datos_bancarios.get()):
            errores.append("Datos Bancarios")

        if not validador.validar_naf(self.numero_seguro_social.get()):
            errores.append("Seguro Social")
            
        if not validador.validadorTelefono(self.telefono.get()):
            errores.append("Teléfono")

        if not validador.validaraSalario(self.salario_mensual.get()):
            errores.append("Salario Mensual")

        if not validador.validarGenero(self.genero.get()):
            errores.append("Género")

        if not validador.validarEmail(self.email.get()):
            errores.append("Email")

        if not validador.validadorGeneral(self.irpf.get()):
            errores.append("IRPF")

        if not validador.validadorGeneral(self.paga_extra.get()):
            errores.append("Paga Extra")

        if not validador.validadorGeneral(self.seg_social.get()):
            errores.append("Seguro Social")

        if errores:
            mensaje_error = "\n".join(errores)
            messagebox.showerror("Validación de campos", mensaje_error)  
            self.validacions.set(mensaje_error)
            return False
        else:
            self.validacions.set("Todos los campos son válidos.")
            return True
