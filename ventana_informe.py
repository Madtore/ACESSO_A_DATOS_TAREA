
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
        barra = ["General", "Hombres", "Mujeres"] 

        self.crear_tarta(self.frameAlta, "Altas", db.num_empleados_alta()[1:], barra[1:])
        self.crear_tarta(self.frameBaja, "Bajas", db.num_empleados_baja()[1:], barra[1:])
        self.crear_grafico(self.frameEdad, "Edad", db.edad_media(), barra)
        self.crear_grafico(self.frameSalario, "Salario", db.retribucion_media(), barra)

        self.frameAlta.pack(fill="both", expand=True)
        
    def crear_tarta(self, frame, titulo, datos, barra):
        
        for i in range(len(datos)):
            if datos[i] == 0:
                datos.remove(datos[i])
                barra.remove(barra[i])
                 
        Label(frame, text=titulo).pack()
        fig, ax = plt.subplots()
        ax.pie(datos, labels=barra, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal') 
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()    

    def crear_grafico(self, frame, titulo, datos, barra):
        datos = list(map(lambda x: 0 if x is None else x, datos))
        Label(frame, text=titulo).pack()
        y_pos = np.arange(len(barra))  
        fig, ax = plt.subplots()  
        ax.bar(y_pos, datos, color=['green', 'blue','pink']) 
        ax.set_xticks(y_pos)
        ax.set_xticklabels(barra)

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def cambia_frame(self, frame):
        self.frameAlta.pack_forget()
        self.frameBaja.pack_forget()
        self.frameEdad.pack_forget()
        self.frameSalario.pack_forget()

        frame.pack(fill="both", expand=True)