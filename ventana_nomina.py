from tkinter import * 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, font
from datetime import datetime
import calendar
from generador_pdf import GeneratorPDF


class VentanaNomina:
    def __init__(self, ventana_principal, empleado , datos):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("1200x1200")
        self.ventana.title("Nómina del Empleado")
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
            12: "Diciembre"
        }
        
       
        main_frame = tk.Frame(self.ventana, bg='white', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        
        header_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(header_frame, text="NÓMINA DEL EMPLEADO", 
                font=('Helvetica', 16, 'bold'), bg='white').pack(pady=10)
        
        
        employee_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        employee_frame.pack(fill=tk.X, pady=(0, 20))
        
        
        tk.Label(employee_frame, text=empleado.apellido_nombre,
                font=('Helvetica', 12, 'bold'), bg='white').pack(anchor=tk.W, padx=10, pady=(10,0))
        tk.Label(employee_frame, text=empleado.direccion,
                font=('Helvetica', 10), bg='white').pack(anchor=tk.W, padx=10)
        
        
        info_frame = tk.Frame(employee_frame, bg='white')
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(info_frame, text=f"NIF: {empleado.nif}",
                font=('Helvetica', 10), bg='white').pack(side=tk.LEFT, padx=5)
        tk.Label(info_frame, text=f"NAF: {empleado.numero_seguro_social}",
                font=('Helvetica', 10), bg='white').pack(side=tk.LEFT, padx=5)
        tk.Label(info_frame, text=f"CCC: {empleado.datos_bancarios}",
                font=('Helvetica', 10), bg='white').pack(side=tk.LEFT, padx=5)
        
        
        period_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        period_frame.pack(fill=tk.X, pady=(0, 20))
        
        mes_actual = datetime.today().month
        dias_mes = calendar.monthrange(datetime.today().year, mes_actual)[1]
        meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 
                6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 
                10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
        
        period_info = tk.Frame(period_frame, bg='white')
        period_info.pack(padx=10, pady=10)
        
        tk.Label(period_info, text=f"Período: {meses[mes_actual]}", bg='white',
                font=('Helvetica', 10)).pack(side=tk.LEFT, padx=20)
        tk.Label(period_info, text=f"Días: {dias_mes}", bg='white',
                font=('Helvetica', 10)).pack(side=tk.LEFT, padx=20)
        tk.Label(period_info, text=f"F. Alta: {empleado.fecha_inicio}", bg='white',
                font=('Helvetica', 10)).pack(side=tk.LEFT, padx=20)
        
        
        salary_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        salary_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(salary_frame, text="CONCEPTOS SALARIALES",
                font=('Helvetica', 12, 'bold'), bg='white').pack(pady=(10,10))
        
       
        self.salario_base = float(empleado.salario_mensual)
        self.base_imponible = float(self.salario_base)
        self.irpf = float(empleado.irpf)
        self.retencion_irpf = float(datos["retencion_irpf"])
        self.prorrata_pagas = float(datos["prorrata_pagas"])
        self.base_mas_prorrata = self.base_imponible + float(self.prorrata_pagas)
        self.cueta_ss = float(empleado.seg_social)
        self.deduccion_ss = float(datos["deduccion_ss"])
        self.total_percibir = float(datos["a_percibir"])
        
        concepts_frame = tk.Frame(salary_frame, bg='white')
        concepts_frame.pack(fill=tk.X, padx=20, pady=(0,10))
        
        for i, (concepto, valor) in enumerate([
            ("Salario Base",self.salario_base),
            ("Base Imponible", self.base_imponible),
            ("BCCC", self.base_mas_prorrata),
            (f"IRPF ({self.irpf}%)", self.retencion_irpf),
            (f"Seguridad Social ({self.cueta_ss}%)", self.deduccion_ss),
            ("Prorrata de Pagas", self.prorrata_pagas)
        ]):
            row_frame = tk.Frame(concepts_frame, bg='white')
            row_frame.pack(fill=tk.X, pady=2)
            tk.Label(row_frame, text=concepto, bg='white',
                    font=('Helvetica', 10)).pack(side=tk.LEFT)
            tk.Label(row_frame, text=f"{valor:,.2f} €", bg='white',
                    font=('Helvetica', 10)).pack(side=tk.RIGHT)
        
       
        total_frame = tk.Frame(main_frame, bg='white', relief=tk.GROOVE, bd=2)
        total_frame.pack(fill=tk.X)
        
        total_inner = tk.Frame(total_frame, bg='white')
        total_inner.pack(fill=tk.X, padx=20, pady=10)
        tk.Label(total_inner, text="TOTAL A PERCIBIR:", bg='white',
                font=('Helvetica', 12, 'bold')).pack(side=tk.LEFT)
        tk.Label(total_inner, text=f"{self.total_percibir:,.2f} €", bg='white',
                font=('Helvetica', 12, 'bold')).pack(side=tk.RIGHT)
        
        
        tk.Button(self.ventana, text="Generar PDF", command=self.generar_pdf, font=('Helvetica', 12, 'bold') ,background='#4169e1', foreground='white').pack(pady=10)
        
        
        
        

    def generar_pdf(self):
        """
        Método para ser llamado desde la interfaz gráfica
        """
        datos_nomina = {
                'salario_base': self.salario_base,
                'base_imponible': self.base_imponible,
                'bccc': self.base_mas_prorrata,
                'irpf': self.irpf,
                'retencion_irpf': self.retencion_irpf,
                'ss': self.cueta_ss,
                'deduccion_ss': self.deduccion_ss,
                'prorrata_pagas': self.prorrata_pagas,
                'total_percibir': self.total_percibir
        }

        generador = GeneratorPDF()
        ruta_pdf = generador.generar_pdf(datos_nomina)
        messagebox.showinfo("PDF Generado", f"El PDF ha sido generado correctamente:\n{ruta_pdf}")
    
        
        