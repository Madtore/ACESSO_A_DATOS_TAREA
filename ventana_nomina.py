from tkinter import * 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, font
from datetime import datetime
import calendar
from fpdf import FPDF


class VentanaNomina:
    def __init__(self, ventana_principal, empleado , datos):
        self.ventana = Toplevel(ventana_principal)
        self.ventana.geometry("1200x800")
        self.ventana.title("Nómina del Empleado")
        self.ventana.grab_set()
        
        self.meses = {
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
        
        self.empleado = empleado
        
        frame = tk.Frame(self.ventana, bg='white', padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        
        titulo_frame = tk.Frame(frame, bg='white', relief=tk.GROOVE, bd=2)
        titulo_frame.pack(fill=tk.X, pady=(0, 20))
        
        
        empleado_frame = tk.Frame(frame, bg='white', relief=tk.GROOVE, bd=2)
        empleado_frame.pack(fill=tk.X, pady=(0, 20))
        
        
        tk.Label(empleado_frame, text=empleado.apellido_nombre,
                font=('Helvetica', 12, 'bold'), bg='white').pack(anchor=tk.W, padx=10, pady=(10,0))
        tk.Label(empleado_frame, text=empleado.direccion,
                font=('Helvetica', 10), bg='white').pack(anchor=tk.W, padx=10)
        
        
        info_frame = tk.Frame(empleado_frame, bg='white')
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(info_frame, text=f"NIF: {empleado.nif}",
                font=('Helvetica', 10), bg='white').pack(side=tk.LEFT, padx=5)
        tk.Label(info_frame, text=f"NAF: {empleado.numero_seguro_social}",
                font=('Helvetica', 10), bg='white').pack(side=tk.LEFT, padx=5)
        tk.Label(info_frame, text=f"CCC: {empleado.datos_bancarios}",
                font=('Helvetica', 10), bg='white').pack(side=tk.LEFT, padx=5)
        
        
        period_frame = tk.Frame(frame, bg='white', relief=tk.GROOVE, bd=2)
        period_frame.pack(fill=tk.X, pady=(0, 20))
        
        mes_actual = datetime.today().month
        dias_mes = calendar.monthrange(datetime.today().year, mes_actual)[1]
        
        
        period = tk.Frame(period_frame, bg='white')
        period.pack(padx=10, pady=10)
        
        tk.Label(period, text=f"Período: {self.meses[mes_actual]}", bg='white',
                font=('Helvetica', 10)).pack(side=tk.LEFT, padx=20)
        tk.Label(period, text=f"Días: {dias_mes}", bg='white',
                font=('Helvetica', 10)).pack(side=tk.LEFT, padx=20)
        tk.Label(period, text=f"F. Alta: {empleado.fecha_inicio}", bg='white',
                font=('Helvetica', 10)).pack(side=tk.LEFT, padx=20)
        
        
        pagas = tk.Frame(frame, bg='white', relief=tk.GROOVE, bd=2)
        pagas.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(pagas, text="CONCEPTOS SALARIALES",
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
        
        concepts_frame = tk.Frame(pagas, bg='white')
        concepts_frame.pack(fill=tk.X, padx=20, pady=(0,10))
        
        for i, (concepto, valor) in enumerate([
            ("Salario Base",self.salario_base),
            ("Base Imponible", self.base_imponible),
            (f"IRPF ({self.irpf}%)", self.retencion_irpf),
            (f"Seguridad Social ({self.cueta_ss}%)", self.deduccion_ss),
            ("Prorrata de Pagas", self.prorrata_pagas)
        ]):
            fila = tk.Frame(concepts_frame, bg='white')
            fila.pack(fill=tk.X, pady=2)
            tk.Label(fila, text=concepto, bg='white',
                    font=('Helvetica', 10)).pack(side=tk.LEFT)
            tk.Label(fila, text=f"{valor:,.2f} €", bg='white',
                    font=('Helvetica', 10)).pack(side=tk.RIGHT)
        
       
        total = tk.Frame(frame, bg='white', relief=tk.GROOVE, bd=2)
        total.pack(fill=tk.X)
        
        total_inserta = tk.Frame(total, bg='white')
        total_inserta.pack(fill=tk.X, padx=20, pady=10)
        tk.Label(total_inserta, text="TOTAL A PERCIBIR:", bg='white',
                font=('Helvetica', 12, 'bold')).pack(side=tk.LEFT)
        tk.Label(total_inserta, text=f"{self.total_percibir:,.2f} €", bg='white',
                font=('Helvetica', 12, 'bold')).pack(side=tk.RIGHT)
        
        
        tk.Button(self.ventana, text="Generar PDF", command=self.generar_pdf, font=('Helvetica', 12, 'bold') ,background='#4169e1', foreground='white').pack(pady=10)
        
        
        
        

    def generar_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 10)
        
        pdf.set_fill_color(255, 255, 255) 
        
        left_margin = 15
        pdf.set_left_margin(left_margin)
        
        pdf.set_line_width(0.5)
        
        pdf.set_xy(left_margin, 30)
        pdf.set_font('Arial', 'B', 10)
        
        pdf.cell(0, 10, self.empleado.apellido_nombre, ln=True)
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 6, self.empleado.direccion, ln=True)
        
        pdf.cell(0, 6, f"NIF: {self.empleado.nif}   NAF: {self.empleado.numero_seguro_social}   CCC: {self.empleado.datos_bancarios}", ln=True)
        
        mes_actual = datetime.today().month
        dias_mes = calendar.monthrange(datetime.today().year, mes_actual)[1]
        
        pdf.ln(10)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 6, f"Período: {self.meses[mes_actual]}   Días: {dias_mes}   F. Alta: {self.empleado.fecha_inicio}", ln=True)
        
        pdf.ln(10)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 10, "CONCEPTOS SALARIALES", ln=True, align='C')
        
        salario_base = float(self.empleado.salario_mensual)
        base_imponible = salario_base
       
        
        salary_concepts = [
            ("Salario Base", salario_base),
            ("Base Imponible", base_imponible),
            (f"IRPF ({self.empleado.irpf}%)", float(self.retencion_irpf)),
            (f"Seguridad Social ({self.empleado.seg_social}%)", float(self.deduccion_ss)),
            ("Prorrata de Pagas", float(self.prorrata_pagas))
        ]
        
        pdf.set_font('Arial', '', 10)
        for concepto, valor in salary_concepts:
            pdf.cell(120, 6, concepto, align='L')
            pdf.cell(0, 6, f"{valor:,.2f} EUR", align='R', ln=True)
        
        pdf.ln(10)
        pdf.set_font('Arial', '', 10)
        total_percibir = float(self.total_percibir)
        pdf.cell(120, 10, "TOTAL A PERCIBIR:", align='L')
        pdf.cell(0, 10, f"{total_percibir:,.2f} EUR", align='R', ln=True)
    
        pdf.output(f'{self.empleado.apellido_nombre}_nomina_{self.meses[mes_actual]}.pdf')
        messagebox.showinfo("PDF Generado", f"El PDF ha sido generado correctamente:\n")
    
        
        