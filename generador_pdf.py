from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from datetime import datetime

class GeneratorPDF:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.elementos = []
        
    def generar_pdf(self, datos_nomina, ruta_salida=None):
        if ruta_salida is None:

            fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
            ruta_salida = f"nomina_{fecha_actual}.pdf"

        doc = SimpleDocTemplate(
            ruta_salida,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm
        )
        
        estilo_titulo = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=30
        )
        
        estilo_concepto = ParagraphStyle(
            'Concepto',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceBefore=5
        )
        
        # Título
        self.elementos.append(Paragraph("Nómina", estilo_titulo))
        self.elementos.append(Spacer(1, 20))
        
        # Crear tabla de conceptos
        datos_tabla = [
            ["Concepto", "Importe"],
            ["Salario Base", f"{datos_nomina['salario_base']:,.2f} €"],
            ["Base Imponible", f"{datos_nomina['base_imponible']:,.2f} €"],
            ["BCCC", f"{datos_nomina['bccc']:,.2f} €"],
            [f"IRPF ({datos_nomina['irpf']}%)", f"{datos_nomina['retencion_irpf']:,.2f} €"],
            [f"Seguridad Social ({datos_nomina['ss']}%)", f"{datos_nomina['deduccion_ss']:,.2f} €"],
            ["Prorrata de Pagas", f"{datos_nomina['prorrata_pagas']:,.2f} €"]
        ]
        
        # Estilo de la tabla
        tabla = Table(datos_tabla, colWidths=[doc.width/2]*2)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ]))
        
        self.elementos.append(tabla)
        self.elementos.append(Spacer(1, 20))
        
        # Total a percibir
        datos_total = [[
            Paragraph("<b>TOTAL A PERCIBIR:</b>", self.styles["Normal"]),
            Paragraph(f"<b>{datos_nomina['total_percibir']:,.2f} €</b>", self.styles["Normal"])
        ]]
        
        tabla_total = Table(datos_total, colWidths=[doc.width/2]*2)
        tabla_total.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (-1, -1), (-1, -1), 'RIGHT'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
        ]))
        
        self.elementos.append(tabla_total)
        
        doc.build(self.elementos)
        return ruta_salida
