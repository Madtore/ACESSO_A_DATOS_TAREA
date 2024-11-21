
from tkinter import *
from data_base import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Ventana_informe:
    def __init__(self, ventana_principal):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.title("Informe")
        self.ventana.geometry("800x600")
        self.ventana.grab_set()
        
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        self.frameAlta = Frame(self.ventana)
        self.frameBaja = Frame(self.ventana)
        self.frameEdad = Frame(self.ventana)
        self.frameSalario = Frame(self.ventana)
        

       
        frameBotton = Frame(self.ventana)
        Button(frameBotton, text="Informe Altas", command=lambda: self.cambia_frame(self.frameAlta)).grid(row=0, column=0, padx=10)
        Button(frameBotton, text="Informe Bajas", command=lambda: self.cambia_frame(self.frameBaja)).grid(row=0, column=1, padx=10)
        Button(frameBotton, text="Informe Edad", command=lambda: self.cambia_frame(self.frameEdad)).grid(row=0, column=2, padx=10)
        Button(frameBotton, text="Informe Salario", command=lambda: self.cambia_frame(self.frameSalario)).grid(row=0, column=3, padx=10)
        frameBotton.pack(pady=10)

        db = DataBase()
        

        self.crear_tarta(self.frameAlta, "Altas", db.num_empleados_alta())
        self.crear_tarta(self.frameBaja, "Bajas", db.num_empleados_baja())
        self.crear_grafico(self.frameEdad, "Edad", db.edad_media())
        self.crear_grafico(self.frameSalario, "Salario", db.retribucion_media())

        self.frameAlta.pack(fill="both", expand=True)
        
    def crear_tarta(self, frame, titulo, datos):
    
        etiquetas = []
        valores = []
        
        for key, value in datos.items():
            print(key, value)
            if key == "empleados":
                continue
            
            if value != 0:
                etiquetas.append(key)
                valores.append(value)
            
        if len(etiquetas) < 1:
            Label(frame, text="Valores no disponibles").pack()
        else:
            Label(frame, text=titulo).pack()
            for i, value in enumerate(valores):
                Label(frame, text=f"{etiquetas[i]}: {value}").pack()
                
            fig, ax = plt.subplots()
            ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
            ax.axis('equal') 
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack()    

    def crear_grafico(self, frame, titulo, datos):
        
        etiquetas = []
        valores = []
        
        for key, value in datos.items():
            print(key, value)
            
            if value != 0:
                etiquetas.append(key)
                valores.append(value)
            
        if len(etiquetas) <= 1:
            Label(frame, text="Valores no disponibles").pack()
        else:
            Label(frame, text=titulo).pack()
            for i, value in enumerate(valores):
                Label(frame, text=f"{etiquetas[i]}: {value}").pack()
            y_pos = np.arange(len(etiquetas))  
            fig, ax = plt.subplots()  
            ax.bar(y_pos, valores, color=['green', 'blue','pink']) 
            ax.set_xticks(y_pos)
            ax.set_xticklabels(etiquetas)

            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

    def cambia_frame(self, frame):
        self.frameAlta.pack_forget()
        self.frameBaja.pack_forget()
        self.frameEdad.pack_forget()
        self.frameSalario.pack_forget()

        frame.pack(fill="both", expand=True)
        
        
    def cerrar_ventana(self):
        plt.close("all")
        self.ventana.destroy() 