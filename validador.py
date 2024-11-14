import re

class Validador():
    def __init__(self):
        pass
    
    def validadorGeneral(self, valor ):
        return valor != ""
    
    def validadorFecha(self, valor ):
        regex = r"^\d{4}-\d{2}-\d{2}$"
        return re.match(regex, valor)
    
    def validadorTelefono(self, valor ):
        regex = r'^\+\d{9}$'
        return re.match(regex, valor)
    
    def validarGenero(self, valor ):
        regex = r'^[MF]$'
        return re.match(regex, valor)
    
    def validaraSalario(self, valor ):
        regex = r'^\d\.\d{2}$'
        return re.match(regex, valor)
    
    def validarEmail(self, valor ):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, valor)
    
    
    
    
    