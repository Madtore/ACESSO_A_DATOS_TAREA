from tkinter import *
from data_base import *
from ventana_baja import *
from ventana_alta import *
from ventana_consulta import *
from ventana_informe import *




def informes():
    ventana = Ventana_informe(principal)
    
def nominas():
    ventana = Ventana_consulta(principal)
    
def altas():
    ventana = Ventana_alta(principal)
    
def bajas():
    ventana = Ventana_baja(principal)
    
base_datos = DataBase()

principal = Tk()
principal.geometry("1400x1200")
principal.title("Aplicación de gestión nóminas")
principal.resizable(0,0)

image = PhotoImage(file="img/nomina.png").subsample(2, 2)
Label(principal, text="").pack()
Label(principal, text="").pack()        
Label(principal, text="").pack()
Label(principal, text="Aplicación de gestión nóminas", font=("Arial", 24)).pack()
Label(principal, text="").pack()
Label(principal, text="").pack()        
Label(principal, text="").pack()       
Label(principal, image=image).pack()
Label(principal, text="").pack()
Label(principal, text="").pack()
Label(principal, text="").pack()
filaBotones = Frame(principal)
filaBotones.pack()

button_stile = {'width': 30, 'height': 5, 'background': '#4169e1', 'font': ('Arial', 16), 'foreground': '#FFFFFF'}

Button(filaBotones, text="Bajas" , command = bajas,**button_stile).grid(row=0, column=0)
Label(filaBotones, text="").grid(row=0, column=1)
Button(filaBotones, text="Altas" ,command = altas, **button_stile).grid(row=0, column=2)

sengundaFilaBotones = Frame(principal)
sengundaFilaBotones.pack(pady=10)

Button(sengundaFilaBotones, text="Informes" ,command = informes, **button_stile).grid(row=0, column=0)
Label(sengundaFilaBotones, text="").grid(row=0, column=1)
Button(sengundaFilaBotones, text="Nóminas" ,command = nominas,  **button_stile).grid(row=0, column=2)


principal.mainloop()